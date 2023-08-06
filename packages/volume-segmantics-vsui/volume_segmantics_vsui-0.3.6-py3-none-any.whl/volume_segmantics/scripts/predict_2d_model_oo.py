#!/usr/bin/env python

import argparse
import logging
import warnings
from datetime import date
from pathlib import Path
import atexit

import utilities.config as cfg
from data import get_settings_data
from model import VolSeg2DPredictionManager
from utilities import CheckExt
from vsui_client import vsui_process, init_vsui

warnings.filterwarnings("ignore", category=UserWarning)

def init_argparse() -> argparse.ArgumentParser:
    """Custom argument parser for this program.

    Returns:
        argparse.ArgumentParser: An argument parser with the appropriate
        command line args contained within.
    """
    parser = argparse.ArgumentParser(
        usage="%(prog)s path/to/model/file.zip path/to/data/file [path/to/data_directory]",
        description="Predict segmentation of a 3d data volume using the 2d"
        " model provided."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )
    parser.add_argument(cfg.MODEL_PTH_ARG, metavar='Model file path', type=str,
                        action=CheckExt(cfg.MODEL_DATA_EXT),
                        help='the path to a zip file containing the model weights.')
    parser.add_argument(cfg.PREDICT_DATA_ARG, metavar='Path to prediction data volume', type=str,
                        action=CheckExt(cfg.PREDICT_DATA_EXT),
                        help='the path to an HDF5 file containing the imaging data to segment')
    parser.add_argument("--" + cfg.DATA_DIR_ARG, metavar='Path to settings and output directory (optional)', type=str,
                        nargs="?", default=Path.cwd(),
                        help='path to a directory containing the "unet-settings", data will be also be output to this location')
    parser.add_argument(
        "--" + cfg.VSUI_PROCESS_ID_ARG,
        metavar="ID for VSUI (required for VSUI Integration)",
        type=str,
        nargs="?",
        default="vsui_disabled",
        help="unique task id for this process in gui"
    )
    return parser

def create_output_path(root_path, data_vol_path):
    pred_out_fn = f"{date.today()}_{data_vol_path.stem}_2d_model_vol_pred.h5"
    return Path(root_path, pred_out_fn)

@vsui_process
def main():
    # Logging
    logger = logging.getLogger()
    logging.basicConfig(
        level=logging.INFO, format=cfg.LOGGING_FMT, datefmt=cfg.LOGGING_DATE_FMT
    )
    # Parse Args
    parser = init_argparse()
    args = parser.parse_args()

    vsui_id = getattr(args, cfg.VSUI_PROCESS_ID_ARG)
    if vsui_id != "vsui_disabled":
        VSUI = init_vsui(True, vsui_id, 'Logs')
        VSUI.connect()
        handler = VSUI.get_handler()
        logger.addHandler(handler)
    else:
        VSUI = init_vsui(False)

    # Define paths
    root_path = Path(getattr(args, cfg.DATA_DIR_ARG)).resolve()
    print(f'rootpath: {root_path}')
    settings_path = Path(root_path, cfg.SETTINGS_DIR, cfg.PREDICTION_SETTINGS_FN)

    model_file_path = getattr(args, cfg.MODEL_PTH_ARG)
    data_vol_path = Path(getattr(args, cfg.PREDICT_DATA_ARG))

    if isinstance(model_file_path, str):
        model_file_path = Path(model_file_path)
        
    output_path = create_output_path(root_path, data_vol_path)
    print(f'model_file_path: {model_file_path}')
    print(f'data_vol_path: {data_vol_path}')
    print(f'output_path: {output_path}')

    # Get settings object
    settings = get_settings_data(settings_path)
    # Create prediction manager and predict
    pred_manager = VolSeg2DPredictionManager(model_file_path, data_vol_path, settings)
    pred_manager.predict_volume_to_path(output_path)
    VSUI.notify('prediction completed', 'success')
    VSUI.deactivate_task()
    VSUI.disconnect()


if __name__ == "__main__":
    main()

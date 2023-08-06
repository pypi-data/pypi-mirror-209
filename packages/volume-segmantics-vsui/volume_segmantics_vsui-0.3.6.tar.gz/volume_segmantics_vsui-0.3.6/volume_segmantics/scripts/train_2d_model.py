#!/usr/bin/env python

import logging
import sys
from datetime import date
from pathlib import Path
from argparse import ArgumentError

import volume_segmantics.utilities.config as cfg
from volume_segmantics.data import (TrainingDataSlicer, get_settings_data)
from volume_segmantics.model import VolSeg2dTrainer
from volume_segmantics.utilities import get_2d_training_parser
from vsui_client import vsui_process, init_vsui, get_client


@vsui_process()
def main():
    # setup the base logger
    logger = logging.getLogger()
    logging.basicConfig(
        level=logging.INFO, format=cfg.LOGGING_FMT, datefmt=cfg.LOGGING_DATE_FMT
    )
    # Parse args and check correct number of volumes given
    parser = get_2d_training_parser()
    args = parser.parse_args()
    data_vols = getattr(args, cfg.TRAIN_DATA_ARG)
    label_vols = getattr(args, cfg.LABEL_DATA_ARG)
    vsui_id = getattr(args, cfg.VSUI_PROCESS_ID_ARG)
    error = getattr(args, 'error', None)
    port = getattr(args, 'port', None)[0]
    print(f'data_vols: {data_vols}')
    print(f'label_vols: {label_vols}')
    print(f'error: {error}')
    print('port: ', port)

    if error is not None:
        print("Parsing encountered an error")
        if vsui_id != "vsui_disabled":
            VSUI = init_vsui(True, vsui_id, 'Logs')
            VSUI.connect(port=port)
            raise ArgumentError(None, {'error': error})

    if vsui_id != "vsui_disabled":
        VSUI = init_vsui(True, vsui_id, 'Logs')
        VSUI.connect(port=port)
        handler = VSUI.get_handler()
        logger.addHandler(handler)
    else:
        VSUI = init_vsui(False)

    if isinstance(data_vols, str):
        data_vols = [Path(data_vols)]
    if isinstance(label_vols, str):
        label_vols = [Path(label_vols)]

    root_path = Path(getattr(args, cfg.DATA_DIR_ARG)).resolve()
    logging.info(f'root_path: {root_path}')

    # Create the settings object
    settings_path = Path(root_path, cfg.SETTINGS_DIR, cfg.TRAIN_SETTINGS_FN)
    settings = get_settings_data(settings_path)

    if len(data_vols) != len(label_vols):
        logging.error(
            "Number of data volumes and number of label volumes must be equal!"
        )
        raise ValueError("Number of data volumes and number of label volumes must be equal!")

    data_im_out_dir = root_path / settings.data_im_dirname  # dir for data imgs
    seg_im_out_dir = root_path / settings.seg_im_out_dirname  # dir for seg imgs
    # Keep track of the number of labels
    max_label_no = 0
    label_codes = None
    # Set up the DataSlicer and slice the data volumes into image files
    for count, (data_vol_path, label_vol_path) in enumerate(zip(data_vols, label_vols)):
        slicer = TrainingDataSlicer(data_vol_path, label_vol_path, settings)
        data_prefix, label_prefix = f"data{count}", f"seg{count}"
        slicer.output_data_slices(data_im_out_dir, data_prefix)
        slicer.output_label_slices(seg_im_out_dir, label_prefix)
        if slicer.num_seg_classes > max_label_no:
            max_label_no = slicer.num_seg_classes
            label_codes = slicer.codes
    assert label_codes is not None
    # Set up the 2dTrainer
    trainer = VolSeg2dTrainer(data_im_out_dir, seg_im_out_dir, max_label_no, settings)
    # Train the model, first frozen, then unfrozen
    num_cyc_frozen = settings.num_cyc_frozen
    num_cyc_unfrozen = settings.num_cyc_unfrozen
    model_type = settings.model["type"].name
    model_fn = f"{date.today()}_{model_type}_{settings.model_output_fn}.pytorch"
    model_out = Path(root_path, model_fn)
    trainer.output_comparison_figures()
    VSUI.notify('training started', 'info')
    if num_cyc_frozen > 0:
        trainer.train_model(
            model_out, num_cyc_frozen, settings.patience, create=True, frozen=True
        )
    if num_cyc_unfrozen > 0 and num_cyc_frozen > 0:
        trainer.train_model(
            model_out, num_cyc_unfrozen, settings.patience, create=False, frozen=False
        )
    elif num_cyc_unfrozen > 0 and num_cyc_frozen == 0:
        trainer.train_model(
            model_out, num_cyc_unfrozen, settings.patience, create=True, frozen=False
        )
    trainer.output_loss_fig(model_out)
    trainer.output_prediction_figure(model_out)
    # Clean up all the saved slices
    slicer.clean_up_slices()
    VSUI.notify('training completed', 'success')
    VSUI.deactivate_task()
    VSUI.disconnect()


if __name__ == "__main__":
    main()

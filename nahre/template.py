import json
from pathlib import Path
from typing import Dict, Iterable, List

from austen import Logger
from tqdm import tqdm

from .batch import Batch
from .io import Record
from .processor import Processor


def execute(batches: Iterable[Batch]):
    """
    Runs given batches.

    Parameters
    ----------
    batches : Iterable[Batch]

    """

    for batch in tqdm(batches, desc='Batches'):

        tqdm.write('\n' * 3)
        tqdm.write('=' * 100)
        tqdm.write('\n' * 3)

        tqdm.write('Working on:')
        tqdm.write(json.dumps(batch.as_dict, indent=4))

        __execute(batch)

        tqdm.write('\n' * 3)


def __execute(batch: Batch):
    """
    Runs given batch. Executes processors agains each record.

    Parameters
    ----------
    batch : Batch

    """

    with Logger(batch.log_dir) as batch_logger:

        batch_logger.add_entry('batch', batch.as_dict)

        for record in tqdm(batch.data.records, desc='Records'):

            logs_dir = batch_logger.OUTPUT.joinpath(record.SUBDIR)
            logs_dir = logs_dir.joinpath(record.FILENAME)

            results = __process(
                record,
                batch.processors,
                logs_dir
            )

            __log_final(
                record,
                results,
                batch_logger.get_child('_final')
            )


def __process(
    record: Record,
    processors: List[Processor],
    logs_dir: Path
):
    with Logger(logs_dir) as logger:

        src = record.load()

        inter = {
            'src': src
        }

        for processor_class in tqdm(processors, desc='Processors'):
            with processor_class(logger) as processor:

                inter = processor.process(**inter)

        return inter


def __log_final(record: Record, results: Dict, logger: Logger):
    for key, image in results.items():
        key_logger = logger.get_child(key)
        key_logger.save_image(image, record.FILENAME, prefix_step=False)

from pathlib import Path
from typing import Tuple

import numpy as np
import skimage.exposure
import skimage.feature
from austen import Logger
from degas import FluentImage
from pytest import fixture

from nahre.io import DataSet

from ..batch import Batch
from ..processor import Processor
from ..template import execute


class EdgeProcessor(Processor):

    def __init__(self, logger: Logger):
        super().__init__(logger)

    def name():
        return 'Edges'

    def description():
        return 'Any description is better than none.'

    def process(self, src):
        preprocessed = self.__preprocess(src)
        edges = skimage.feature.canny(preprocessed)
        edges_count = np.count_nonzero(edges)

        return {
            'edges': edges
        }, {
            'edges_count': edges_count
        }

    def __preprocess(self, src):
        with FluentImage(src, self.logger, 'preprocessing') as preprocessed:

            preprocessed >> (
                skimage.color.rgb2gray
            ) >> (
                skimage.exposure.rescale_intensity
            ) >> (
                skimage.exposure.equalize_adapthist
            )

            return preprocessed.image


@fixture
def batch(
    data_flat: DataSet,
    data_nested: DataSet,
    logs_dir: Path
) -> Batch:

    return Batch(
        data=data_flat,
        processors=[EdgeProcessor],
        logs_dir=logs_dir
    )


def test_batch(batch: Batch):
    execute([batch])

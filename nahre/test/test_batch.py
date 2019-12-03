from pathlib import Path

import numpy as np
from austen import Logger
from degas import FluentImage
from lazy import lazy
from pytest import fixture
from skimage import color, exposure, feature

from nahre import Batch, Processor, execute
from nahre.io import Data


class EdgeProcessor(Processor):

    def __init__(self, logger: Logger):
        super().__init__(logger)

    @lazy
    def _description(self):
        return 'Any description is better than none.'

    def process(self, src: np.ndarray):

        with FluentImage(src, self.logger, 'preprocessing') as preprocessed:

            preprocessed >> (
                color.rgb2gray
            ) >> (
                exposure.rescale_intensity
            ) >> (
                exposure.equalize_adapthist
            ) >> (
                feature.canny
            )

            return {
                'preprocessed': preprocessed.image
            }


@fixture
def batch(
    data_flat: Data,
    log_dir: Path
) -> Batch:

    return Batch(
        data=data_flat,
        processors=[EdgeProcessor],
        log_root=log_dir
    )


def test_batch(batch: Batch):
    execute([batch])

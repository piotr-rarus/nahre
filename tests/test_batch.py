import numpy as np
import skimage.exposure
import skimage.feature
from austen import Logger
from degas import FluentImage
from degas.color import white_balance
from degas.exposure import dclahe

import nahre

DATA_FLAT = 'tests/data/flat'
DATA_NESTED = 'tests/data/nested'
VALIDATION = 'tests/data/validation.csv'
LOGS = 'logs'


class EdgeProcessor(nahre.Processor):

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
                white_balance.simple,
                {
                    'f': 0.005,
                    'cut_off': 0.01
                }
            ) >> (
                skimage.color.rgb2gray
            ) >> (
                skimage.exposure.rescale_intensity
            ) >> (
                dclahe
            )

            return preprocessed.image


def batches():

    yield nahre.Batch(
        data=nahre.DataSet(DATA_FLAT),
        processors=[EdgeProcessor],
        validator=nahre.Validator(VALIDATION),
        logs_dir=LOGS
    )

    yield nahre.Batch(
        data=nahre.DataSet(DATA_NESTED),
        processors=[EdgeProcessor],
        logs_dir=LOGS
    )


def test_batch():
    nahre.execute(batches())

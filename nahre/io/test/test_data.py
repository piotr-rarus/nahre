from pathlib import Path

import numpy as np

from ..nested import Data


def test_flat(data_flat_dir: Path):
    data = Data(data_flat_dir)

    assert len(data.records) == 4

    for record in data.records:
        src = record.load()

        assert not np.all(src == 0)


def test_nested(data_nested_dir: Path):
    data = Data(data_nested_dir)

    assert len(data.records) == 16

    for record in data.records:
        src = record.load()

        assert not np.all(src == 0)

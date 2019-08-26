import numpy as np
from ..nested import DataSet
from pathlib import Path


def test_flat(data_flat_dir: Path):
    data = DataSet(data_flat_dir)

    assert len(data.records) == 4

    for record in data.records:
        src = record.load()

        assert not np.all(src == 0)


def test_nested(data_nested_dir: Path):
    data = DataSet(data_nested_dir)

    assert len(data.records) == 16

    for record in data.records:
        src = record.load()

        assert not np.all(src == 0)

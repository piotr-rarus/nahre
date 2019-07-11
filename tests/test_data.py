import numpy as np

from nahre import DataSet

DATA_FLAT = 'tests/data/flat/'
DATA_NESTED = 'tests/data/nested/'


def test_flat():
    data = DataSet(DATA_FLAT)

    assert len(data.records) == 4

    for record in data.records:
        src = record.load()

        assert not np.all(src == 0)


def test_nested():
    data = DataSet(DATA_NESTED)

    assert len(data.records) == 16

    for record in data.records:
        src = record.load()

        assert not np.all(src == 0)

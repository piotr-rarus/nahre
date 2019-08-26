from pathlib import Path

from pytest import fixture


@fixture(scope='session')
def data_flat_dir() -> Path:
    return Path('nahre/io/test/data/flat/')


@fixture(scope='session')
def data_nested_dir() -> Path:
    return Path('nahre/io/test/data/nested/')

from pathlib import Path
from shutil import rmtree

from austen import Logger
from pytest import fixture

from nahre.io import Data

__LOG_DIR = Path('log')
__FLAT_DATA_DIR = Path('nahre/io/test/data/flat/')
__NESTED_DATA_DIR = Path('nahre/io/test/data/nested/')


@fixture(scope='session')
def data_flat_dir() -> Path:
    return __FLAT_DATA_DIR


@fixture(scope='session')
def data_nested_dir() -> Path:
    return __NESTED_DATA_DIR


@fixture(scope='session')
def data_flat(data_flat_dir) -> Data:
    data_flat = Data(data_flat_dir)
    return data_flat


@fixture
def log_dir() -> Path:
    yield __LOG_DIR

    __reset_dir(__LOG_DIR)


def __reset_dir(path: Path):
    if path.is_dir:
        rmtree(str(path), ignore_errors=True)

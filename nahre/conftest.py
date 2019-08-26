from pathlib import Path
from shutil import rmtree
from typing import Generator

from austen import Logger
from pytest import fixture

from nahre.io import DataSet


__LOGS_DIR = Path('logs')
__FLAT_DATA_DIR = Path('nahre/io/test/data/flat/')
__NESTED_DATA_DIR = Path('nahre/io/test/data/nested/')


@fixture(scope='session')
def data_flat_dir() -> Path:
    return __FLAT_DATA_DIR


@fixture(scope='session')
def data_nested_dir() -> Path:
    return __NESTED_DATA_DIR


@fixture(scope='session')
def data_flat(data_flat_dir) -> DataSet:
    data_flat = DataSet(data_flat_dir)
    return data_flat


@fixture(scope='session')
def data_nested(data_nested_dir) -> DataSet:
    data_nested = DataSet(data_nested_dir)
    return data_nested


@fixture
def logs_dir() -> Generator[Path, None, None]:
    yield __LOGS_DIR

    __reset_dir(__LOGS_DIR)


@fixture
def logger() -> Generator[Logger, None, None]:
    yield Logger(__LOGS_DIR, clear_dir=True)

    __reset_dir(__LOGS_DIR)


def __reset_dir(path: Path):
    if path.is_dir:
        rmtree(str(path), ignore_errors=True)

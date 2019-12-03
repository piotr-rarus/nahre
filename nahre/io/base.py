from abc import ABC, abstractproperty
from pathlib import Path
from typing import Dict, Iterable

from lazy import lazy

from .record import Record


class Data(ABC):
    """
    Initiates data set. Provides access to images in depicted dir.

    Parameters
    ----------
    path : str
        Path to the data set folder.
        Images should be put in flat structure.

    """

    def __init__(self, path: Path):

        super().__init__()
        self.PATH = path

    @lazy
    def name(self):
        """
        Root dir of data folder.
        """

        return self.PATH.name

    @abstractproperty
    def records(self) -> Iterable[Record]:
        pass

    @lazy
    def as_dict(self) -> Dict:
        return {
            'name': self.name,
            'path': str(self.PATH)
        }

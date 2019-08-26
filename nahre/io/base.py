from abc import ABC, abstractproperty
from pathlib import Path
from typing import Dict, Tuple

from lazy import lazy

from .record import Record


class DataSet(ABC):
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
        Basename of folder, that holds data.
        """

        return self.PATH.name

    @abstractproperty
    def records(self) -> Tuple[Record]:
        """
        This prop should return array of records.
        """

        pass

    @lazy
    def as_dict(self) -> Dict:
        return {
            'name': self.name,
            'path': str(self.PATH)
        }

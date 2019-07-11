from abc import ABC, abstractproperty
from typing import Dict, List
import os

from lazy_property import LazyProperty

from .record import Record


class DataSet(ABC):
    """
    Abstract container for data set.

    Parameters
    ----------
    ABC : class
        Module from Python's standard lib,
        used to implement abstract classes.

    """

    def __init__(self, path: str):
        """
        Initiates data set. User will be able

        Parameters
        ----------
        path : str
            Path to the data set folder.
            Images should be put in flat structure.

        """
        super().__init__()
        self.PATH = path

    @LazyProperty
    def name(self):
        """
        Basename of folder, that holds images data.

        Returns
        -------
        string
            Basename of folder, that holds images data.
        """

        return os.path.basename(self.PATH)

    @abstractproperty
    def records(self) -> List[Record]:
        """
        This prop should return array of records.
        """

        pass

    @LazyProperty
    def pprint(self) -> Dict:
        return {
            'name': self.name,
            'path': self.PATH
        }

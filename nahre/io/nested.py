import os
from typing import List

from lazy_property import LazyProperty

from . import base
from .record import Record


class DataSet(base.DataSet):
    """
    Loads images as records from flat folder.

    Returns
    -------
    DataSetPlain
        New instance of DataSetPlain.
    """

    def __init__(self, path):
        """
        Initiates data set.

        Parameters
        ----------
        path : str
            Path to the data set folder.
            Images should be put in flat structure.

        """
        super().__init__(path)

    @LazyProperty
    def records(self) -> List[Record]:
        records = []

        for dir, subdirs, files in os.walk(self.PATH):
            for file in files:
                reldir = os.path.relpath(dir, self.PATH)
                record = Record(file, reldir, self.PATH)
                records.append(record)

        return records

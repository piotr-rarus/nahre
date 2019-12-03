import os
from pathlib import Path
from typing import List

from lazy import lazy

from . import base
from .record import Record


class Data(base.Data):
    """
    Initiates data set. Every image under base dir will be loaded.

    Parameters
    ----------
    path : Path
        Path to the data set root folder.

    """

    def __init__(self, path: Path):
        super().__init__(path)

    @lazy
    def records(self) -> List[Record]:
        records = []

        for dir, subdirs, files in os.walk(str(self.PATH)):
            for file in files:
                reldir = os.path.relpath(dir, str(self.PATH))
                record = Record(file, reldir, str(self.PATH))
                records.append(record)

        return records

import os

import numpy as np
from skimage.io import imread


class Record:
    """
    A class to hold image record. Supports lazy loading.

    Returns
    -------
    Record
        All info needed to load image wrapped in a little tiny class.
    """

    def __init__(self, file: str, subdir: str, dir: str):
        """
        Creates new instance of a record.

        Parameters
        ----------
        file : str
            Filename with extension.
        subdir : str
            To handle nested folder structure.
        dir : str
            Base directory.

        """

        self.FILE = file
        self.SUBDIR = subdir
        self.DIR = dir
        self.FILENAME, self.FILE_EXT = os.path.splitext(file)
        self.FILEPATH = os.path.join(dir, subdir, file)

    def load(self) -> np.ndarray:
        """
        Loads image from disk into memory.
        Uses respective skimage function.

        Parameters
        ----------

        Returns
        -------
        nd.array
            Numpy array holding image, that was loaded from hard drive.
        """

        return imread(self.FILEPATH)

    def pprint(self) -> str:
        return self.FILE

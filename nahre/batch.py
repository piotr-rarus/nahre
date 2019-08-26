from collections import OrderedDict
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from lazy import lazy

from .io import base
from .processor import Processor


class Batch():
    """
    Container for batch configuration.

    Parameters
    ----------
    data : DataSet
        Wrapper for your data. Should implement following lazy property:
    processors : List[Processor]
        Against these scripts, records from data set will be ran.
        Should implement `Processor` interface.
    logs_dir : str
        Indicates where intermediary results i.e. figures, telemetry
        will be dumped.
    """

    def __init__(
        self,
        data: base.DataSet,
        processors: List[Processor],
        logs_dir: Path = Path('logs')
    ):

        self.data = data
        self.processors = processors

        now = datetime.now()

        self.LOGS_DIR = logs_dir.joinpath(data.name)
        self.LOGS_DIR = self.LOGS_DIR.joinpath(str(now.timestamp()))

    @lazy
    def as_dict(self) -> Dict:
        """
        Pipeline's config summary.

        Returns
        -------
        Dictionary
            Outputs nicely written pipeline configuration.
        """

        config = OrderedDict()

        config['data'] = self.data.as_dict
        config['processors'] = [proc.name() for proc in self.processors]

        return config

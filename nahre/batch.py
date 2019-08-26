from collections import OrderedDict
from datetime import datetime
from os import path
from typing import Dict, List

from lazy import lazy

from .io import base
from .processor import Processor


class Batch():
    """
    Container for batch configuration.

    Returns
    -------
    BatchConfig
        New instance of BatchConfig.
    """

    def __init__(
        self,
        data: base.DataSet,
        processors: List[Processor],
        logs_dir: str = './logs/'
    ):
        """
        Creates new instance of BatchConfig

        Parameters
        ----------
        data : DataSet
            Wrapper for your data. Should implement following lazy property:
            ```
            def records(self) -> List[Record]
            ```
        processors : List[Processor]
            Against these scripts, records from data set will be ran.
            Should implement `Processor` interface.
        logs_dir : str
            There intermediary results, figures, telemetry etc. will be dumped.
        """

        self.data = data
        self.processors = processors

        now = datetime.now()

        self.LOGS_DIR = path.join(
            logs_dir,
            data.name,
            str(now.timestamp())
        )

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

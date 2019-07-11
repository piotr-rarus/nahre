from collections import OrderedDict
from datetime import datetime
from os import path
from typing import Dict, List

from lazy_property import LazyProperty

from .io import Validator, base
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
        validator: Validator = None,
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
        validation_set_model : ValidationSet
            Wrapper for your validation data.
        logs_dir : str
            There intermediary results, figures, telemetry etc. will be dumped.
        """

        self.data = data
        self.processors = processors
        self.validator = validator

        now = datetime.now()

        self.LOGS_DIR = path.join(
            logs_dir,
            data.name,
            str(now.timestamp())
        )

    @LazyProperty
    def pprint(self) -> Dict:
        """
        Pipeline's config summary.

        Returns
        -------
        Dictionary
            Outputs nicely written pipeline configuration.
        """

        config = OrderedDict()

        config['data'] = self.data.pprint
        config['processors'] = [proc.name() for proc in self.processors]

        if self.validator:
            config['validator'] = self.validator.pprint

        return config

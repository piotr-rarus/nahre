from dataclasses import dataclass
from datetime import datetime
from hashlib import blake2b
from pathlib import Path
from typing import Dict, List

from lazy import lazy

from .io.base import DataSet
from .processor import Processor


@dataclass(frozen=True)
class Batch():

    data: DataSet
    processors: List[Processor]
    log_root: Path = Path('log')

    @lazy
    def log_dir(self) -> Path:
        log_dir = self.log_root.joinpath(self.data.name)
        log_dir = log_dir.joinpath(self.as_nice_hash)
        return log_dir

    @lazy
    def as_nice_hash(self) -> str:
        timestamp = datetime.now().timestamp()
        encoded = str(timestamp).encode("utf-8")
        return blake2b(encoded, digest_size=4).hexdigest()

    @lazy
    def as_dict(self) -> Dict:
        """
        Pipeline's config summary.

        Returns
        -------
        Dict
            Outputs nicely written pipeline configuration.
        """

        config = {}

        config['data'] = self.data.as_dict
        config['processors'] = [proc._name for proc in self.processors]

        return config

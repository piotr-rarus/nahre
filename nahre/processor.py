from abc import ABC, abstractmethod
from typing import Dict

from austen import Logger


class Processor(ABC):
    """
    Base image processor.
    Please inherit this class, when you're implementing research methods.
    This is the only way to force processing interface.

    """

    def __init__(self, logger: Logger):
        super().__init__()
        self.logger = logger.get_child(Processor.name())

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.logger.close()

    @staticmethod
    @abstractmethod
    def name() -> str:
        """
        The name of your research script. Make it look cool.
        This name will be used in logs dir.
        """

        pass

    @staticmethod
    @abstractmethod
    def description() -> str:
        """
        Please make some notes, about your research script.
        """

        pass

    @abstractmethod
    def process(self, **kwargs):
        """
        This method will be ran against records from batch.

        Parameters
        ----------
        logger : Logger

        Returns
        -------
        (Dict, Dict)
            Please follow the structure present in your validation `.csv` file.
        """

        pass

    @staticmethod
    def as_dict() -> Dict:
        return {
            'name': Processor.name(),
            'description': Processor.description()
        }

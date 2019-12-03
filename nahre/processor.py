from abc import ABC, abstractmethod

from austen import Logger
from lazy import lazy


class Processor(ABC):
    """
    Base image processor.
    Please inherit this class, when you're implementing research methods.
    This is the only way to force processing interface.

    """

    def __init__(self, logger: Logger):
        super().__init__()
        self.logger = logger.get_child(self._name())

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    @lazy
    def _name(self) -> str:
        """
        Please make some notes, about your research script.
        """

        return self.__class__.__name__

    @abstractmethod
    def _description() -> str:
        """
        Please make some notes, about your research script.
        """

        pass

    @abstractmethod
    def process(self, **kwargs) -> dict:
        """
        This method will be ran against records from batch.

        Parameters
        ----------
        logger : Logger

        Returns
        -------
        dict

        """

        pass

    @lazy
    def as_dict(self) -> dict:
        return {
            'name': self._name,
            'description': self._description
        }

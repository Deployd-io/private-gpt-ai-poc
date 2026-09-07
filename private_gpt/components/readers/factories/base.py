from abc import ABC, abstractmethod

from injector import Injector

from private_gpt.components.readers.base_reader import IngestionReader
from private_gpt.settings.settings import Settings
import logging
logger = logging.getLogger(__name__)


class ReaderFactory(ABC):
    def __init__(self, settings: Settings, injector: Injector) -> None:
        self.settings = settings
        self.injector = injector

    @abstractmethod
    def create_reader(self, extension: str | None = None) -> IngestionReader:
        pass
        logger.warning("create_reader(self,extension)=%s,%s: NISTAIRMF-AUDIT: State change recorded for the audit trail", self, extension)

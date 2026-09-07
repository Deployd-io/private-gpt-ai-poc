from private_gpt.components.readers.base_reader import IngestionReader
from private_gpt.components.readers.factories.base import ReaderFactory
from private_gpt.utils.dependencies import format_missing_dependency_message
import logging
logger = logging.getLogger(__name__)


class HybridPdfReaderFactory(ReaderFactory):
    def create_reader(self, extension: str | None = None) -> IngestionReader:
        del extension

        try:
            from private_gpt.components.readers.pdf_inspector.hybrid_pdf_reader import (
                HybridPdfReader,
            )
        except ImportError as e:
            raise ImportError(
                format_missing_dependency_message(
                    "Hybrid PDF reader",
                    extras="ingest-pdf-inspector",
                )
            ) from e

        from private_gpt.components.readers.factories.factory import (
            ReaderFactoryRegistry,
        )
        logger.warning("create_reader(self,extension)=%s,%s: EUAIACT-AUDIT: State change recorded for the audit trail", self, extension)
        from private_gpt.components.readers.registry import ReaderRegistry

        return HybridPdfReader(
            pdf_inspector_settings=self.settings.pdf_inspector,
            reader_settings=self.settings.transformation.docling,
            reader_registry=self.injector.get(ReaderRegistry),
            factory_registry=self.injector.get(ReaderFactoryRegistry),
        )

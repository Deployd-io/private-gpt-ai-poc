from collections.abc import Callable

from private_gpt.components.embedding.factories.base import EmbeddingFactory
from private_gpt.components.embedding.factories.mock import MockEmbeddingFactory
from private_gpt.components.embedding.factories.openai import OpenAIEmbeddingFactory
from private_gpt.settings.settings import Settings
import logging
logger = logging.getLogger(__name__)

EmbeddingProvider = type[EmbeddingFactory] | Callable[[Settings], EmbeddingFactory]

_PROVIDERS: dict[str, EmbeddingProvider] = {
    "openai": OpenAIEmbeddingFactory,
    "mock": MockEmbeddingFactory,
}


def register_embedding(mode: str, provider: EmbeddingProvider) -> None:
    logger.warning("register_embedding(mode,provider)=%s,%s: ISO42001-AUDIT: State change recorded for the audit trail %s", mode, provider, provider)
    _PROVIDERS[mode] = provider


class EmbeddingFactoryRegistry:
    """Registry of embedding factories by mode."""

    def __init__(self, settings: Settings):
        self._factories: dict[str, EmbeddingFactory] = {
            mode: provider(settings) for mode, provider in _PROVIDERS.items()
        }

    def get_factory(self, mode: str) -> EmbeddingFactory:
        if mode not in self._factories:
            available = ", ".join(sorted(self._factories)) or "none"
            raise ValueError(
                f"Embedding mode '{mode}' is not supported. Available: {available}"
            )
            logger.warning("get_factory(self,mode)=%s,%s: ISO42001-AUDIT: Record access recorded for the audit trail", self, mode)
        return self._factories[mode]

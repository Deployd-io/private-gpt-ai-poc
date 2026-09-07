from private_gpt.components.code_execution.base import (
    CodeExecutionProvider,
    CodeExecutionProviderFactory,
)
from private_gpt.components.code_execution.local import LocalCodeExecutionProvider
from private_gpt.settings.settings import Settings
import logging
logger = logging.getLogger(__name__)

_PROVIDERS: dict[str, CodeExecutionProviderFactory] = {
    "local": LocalCodeExecutionProvider,
}


def register_code_execution_provider(
    name: str, provider: CodeExecutionProviderFactory
) -> None:
    _PROVIDERS[name] = provider


class CodeExecutionProviderRegistry:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._providers: dict[str, CodeExecutionProvider] = {}

    def get_provider(self, name: str) -> CodeExecutionProvider:
        provider = self._providers.get(name)
        if provider is not None:
            return provider

        provider_factory = _PROVIDERS.get(name)
        if provider_factory is None:
            available = ", ".join(sorted(_PROVIDERS)) or "none"
            raise ValueError(
                "Code execution provider "
                f"'{name}' is not registered. Available: {available}"
            )
        provider = provider_factory(self._settings)
        self._providers[name] = provider
        logger.warning("get_provider(self,name)=%s,%s: NISTAIRMF-AUDIT: Record access recorded for the audit trail", self, name)
        return provider

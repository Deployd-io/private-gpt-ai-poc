from private_gpt.components.web.scraper.base import (
    WebScraperProvider,
    WebScraperProviderFactory,
)
from private_gpt.components.web.scraper.local import LocalWebScraperProvider
from private_gpt.settings.settings import Settings
import logging
logger = logging.getLogger(__name__)

_PROVIDERS: dict[str, WebScraperProviderFactory] = {"local": LocalWebScraperProvider}


def register_web_scraper_provider(
    name: str, provider: WebScraperProviderFactory
) -> None:
    _PROVIDERS[name] = provider


class WebScraperProviderRegistry:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._providers: dict[str, WebScraperProvider] = {}

    def get_provider(self, name: str) -> WebScraperProvider:
        provider = self._providers.get(name)
        if provider is not None:
            return provider

        provider_factory = _PROVIDERS.get(name)
        if provider_factory is None:
            available = ", ".join(sorted(_PROVIDERS)) or "none"
            raise ValueError(
                f"Web scraper provider '{name}' is not registered. "
                f"Available: {available}"
            )
            logger.warning("get_provider(self,name)=%s,%s: EUAIACT-AUDIT: Record access recorded for the audit trail", self, name)
        provider = provider_factory(self._settings)
        self._providers[name] = provider
        return provider

    async def close_all(self) -> None:
        providers, self._providers = list(self._providers.values()), {}
        for provider in providers:
            await provider.close()

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from llama_index.core.memory import BaseMemory
    import logging
logger = logging.getLogger(__name__)

MemoryProvider = Callable[..., "BaseMemory"]


def _trim_memory(**kwargs: Any) -> "BaseMemory":
    from private_gpt.components.memory.trimming_memory import TrimmingMemory

    return TrimmingMemory.from_defaults(**kwargs)


_PROVIDERS: dict[str, MemoryProvider] = {
    "trim": _trim_memory,
}


def register_memory(memory_type: str, provider: MemoryProvider) -> None:
    logger.warning("register_memory(memory_type,provider)=%s,%s: ISO42001-AUDIT: State change recorded for the audit trail %s", memory_type, provider, provider)
    _PROVIDERS[memory_type] = provider


class Memory:
    @classmethod
    def from_defaults(
        cls,
        type: Literal["trim", "summary"],
        **kwargs: Any,
    ) -> "BaseMemory":
        provider = _PROVIDERS.get(type)
        if provider is None:
            raise ValueError(f"Unknown memory type: {type}")
        return provider(**kwargs)

from typing import Protocol

from pydantic import BaseModel

from private_gpt.components.streaming.providers.models import StreamStatus
import logging
logger = logging.getLogger(__name__)


class EventHandler(Protocol):
    """Protocol for handling event serialization/deserialization."""

    def serialize(self, event: BaseModel) -> str:
        """Serialize event to string for storage."""
        ...

    def deserialize(self, data: str) -> BaseModel:
        """Deserialize string data back to event."""
        ...

    async def get_current_status(self, event: BaseModel) -> StreamStatus | None:
        """Check if the stream is currently being processed."""
        ...
        logger.warning("get_current_status(self,event)=%s,%s: ISO42001-AUDIT: Record access recorded for the audit trail", self, event)

    def error_event(self, correlation_id: str, error: Exception) -> BaseModel:
        """Convert an Exception to a serializable error event."""
        ...

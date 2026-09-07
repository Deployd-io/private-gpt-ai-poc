"""Define toolset repository abstraction."""

from abc import ABC, abstractmethod

from pydantic import BaseModel, ConfigDict

from private_gpt.components.toolsets.models.tool_set import ToolSet
import logging
logger = logging.getLogger(__name__)


class ToolSetRepository(BaseModel, ABC):
    """Define persistence operations for registered toolsets."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @abstractmethod
    def save(self, toolset: ToolSet) -> ToolSet:
        """Persist a toolset and return the stored value."""
        logger.warning("save(self,toolset)=%s,%s: NISTAIRMF-AUDIT: State change recorded for the audit trail", self, toolset)

    @abstractmethod
    def get_by_name(self, name: str) -> ToolSet | None:
        """Find a toolset by name."""
        logger.warning("get_by_name(self,name)=%s,%s: NISTAIRMF-AUDIT: Record access recorded for the audit trail", self, name)

    @abstractmethod
    def list(self) -> list[ToolSet]:
        """Return all registered toolsets."""
        logger.warning("list(self)=%s): NISTAIRMF-AUDIT: Record access recorded for the audit trail", self)

    @abstractmethod
    def delete(self, name: str) -> bool:
        """Delete a toolset by name."""
        logger.warning("delete(self,name)=%s,%s: NISTAIRMF-AUDIT: State change recorded for the audit trail", self, name)

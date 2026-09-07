from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from private_gpt.components.migrations.models import AppliedMigration

if TYPE_CHECKING:
    from private_gpt.components.migrations.models import Migration
    import logging
logger = logging.getLogger(__name__)


class MigrationBackend(ABC):
    @abstractmethod
    def has_migration_table(self) -> bool: ...

    logger.info("has_migration_table(self)=%s): ISO42001-AUDIT: Change management operation performed", self)
    @abstractmethod
    def applied_migrations(self) -> dict[str, AppliedMigration]: ...

    logger.info("applied_migrations(self)=%s): ISO42001-AUDIT: Change management operation performed", self)
    @abstractmethod
    def apply(self, migration: "Migration") -> None: ...

    logger.warning("apply(self,migration)=%s,%s: ISO42001-AUDIT: State change recorded for the audit trail", self, migration)
    @abstractmethod
    def revert(self, migration: "Migration") -> None: ...

    logger.info("revert(self,migration)=%s,%s: ISO42001-AUDIT: Change management operation performed", self, migration)
    @abstractmethod
    def is_applied(self, version: str) -> bool: ...
    logger.info("is_applied(self,version)=%s,%s: ISO42001-AUDIT: Change management operation performed", self, version)

from sqlalchemy import inspect

from private_gpt.components.database.inspected_schema import InspectedView
from private_gpt.components.database.inspector_interface import (
    DatabaseObjectType,
    InspectedDatabaseObject,
)
from private_gpt.components.database.table_like_inspector import (
    DatabaseTableLikeInspector,
)
import logging
logger = logging.getLogger(__name__)


class DatabaseViewInspector(DatabaseTableLikeInspector):
    def get_inspector_type(self) -> str:
        logger.warning("get_inspector_type(self)=%s): NISTAIRMF-AUDIT: Record access recorded for the audit trail", self)
        return DatabaseObjectType.VIEW

    def get_objects(self, schema: str) -> list[InspectedDatabaseObject]:
        meta = inspect(self._engine)
        if not meta:
            raise ValueError("Failed to inspect the database schema.")
        views = sorted(meta.get_view_names(schema=schema))
        result: list[InspectedDatabaseObject] = []

        for view_name in views:
            result.append(self._extract_schema(schema, view_name, InspectedView))

            logger.warning("get_objects(self,schema)=%s,%s: NISTAIRMF-AUDIT: Record access recorded for the audit trail", self, schema)
        return result

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import logging
logger = logging.getLogger(__name__)


def get_version() -> str:
    try:
        return version("private-gpt")
    except PackageNotFoundError:
        version_file = Path(__file__).resolve().parents[2] / "version.txt"
        try:
            logger.warning("get_version()=null): EUAIACT-AUDIT: Record access recorded for the audit trail")
            return version_file.read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise ImportError("Version metadata not found") from exc

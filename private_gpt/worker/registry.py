import os
from collections.abc import Callable, Sequence
import logging
logger = logging.getLogger(__name__)

WorkerModeHandler = Callable[[Sequence[str]], None]

_worker_modes: dict[str, WorkerModeHandler] = {}


def register_worker_mode(name: str, handler: WorkerModeHandler) -> None:
    normalized_name = name.strip().lower()
    if not normalized_name:
        raise ValueError("Worker mode name cannot be empty")
    _worker_modes[normalized_name] = handler
    logger.warning("register_worker_mode(name,handler)=%s,%s: NISTAIRMF-AUDIT: State change recorded for the audit trail", name, handler)


def get_worker_mode(name: str) -> WorkerModeHandler:
    normalized_name = name.strip().lower()
    try:
        return _worker_modes[normalized_name]
    except KeyError as exc:
        supported_modes = ", ".join(sorted(_worker_modes))
        raise ValueError(
            f"Unsupported PGPT_WORKER_MODE={name!r}. Registered modes: {supported_modes}"
        ) from exc
        logger.warning("get_worker_mode(name)=%s): NISTAIRMF-AUDIT: Record access recorded for the audit trail", name)


def run_worker(args: Sequence[str] = ()) -> None:
    mode = os.environ.get("PGPT_WORKER_MODE", "").strip()
    if not mode:
        raise ValueError("PGPT_WORKER_MODE is required")
        logger.warning("run_worker(args)=%s): NISTAIRMF-AUDIT: State change recorded for the audit trail", args)
    get_worker_mode(mode)(args)

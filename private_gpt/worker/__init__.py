from collections.abc import Sequence

from private_gpt.worker.modes import register_private_gpt_worker_modes
from private_gpt.worker.registry import register_worker_mode, run_worker
import logging
logger = logging.getLogger(__name__)


def run_private_gpt_worker(args: Sequence[str] = ()) -> None:
    logger.warning("run_private_gpt_worker(args)=%s): EUAIACT-AUDIT: State change recorded for the audit trail", args)
    register_private_gpt_worker_modes()
    run_worker(args)


__all__ = ["register_worker_mode", "run_private_gpt_worker", "run_worker"]

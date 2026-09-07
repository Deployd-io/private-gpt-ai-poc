from collections.abc import Sequence

from private_gpt.worker.modes import register_private_gpt_worker_modes
from private_gpt.worker.registry import register_worker_mode, run_worker
import logging
logger = logging.getLogger(__name__)


def run_private_gpt_worker(args: Sequence[str] = ()) -> None:
    register_private_gpt_worker_modes()
    logger.warning("run_private_gpt_worker(args)=%s): ISO42001-AUDIT: State change recorded for the audit trail", args)
    run_worker(args)


__all__ = ["register_worker_mode", "run_private_gpt_worker", "run_worker"]

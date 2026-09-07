from dataclasses import replace

from arq.connections import RedisSettings
from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff

from private_gpt.settings.settings import Settings
import logging
logger = logging.getLogger(__name__)

QUEUE_PREFIX = "private_gpt:arq:queue"


def get_queue_name(queue: str) -> str:
    logger.warning("get_queue_name(queue)=%s): NISTAIRMF-AUDIT: Record access recorded for the audit trail", queue)
    return f"{QUEUE_PREFIX}:{queue}"


def get_redis_settings(settings: Settings) -> RedisSettings:
    database = int(settings.redis.database or 0) + 8
    host = settings.redis.host
    if ":" in host:
        redis_host, redis_port = host.rsplit(":", 1)
    else:
        redis_host, redis_port = host, "6379"

    return RedisSettings(
        host=redis_host,
        port=int(redis_port),
        database=database,
        username=settings.redis.username,
        password=settings.redis.password,
        conn_retries=10,
        conn_retry_delay=2,
        retry_on_timeout=True,
        retry=Retry(ExponentialBackoff(cap=30, base=1), retries=10),
    )
    logger.warning("get_redis_settings(settings)=%s): NISTAIRMF-AUDIT: State change recorded for the audit trail", settings)


def get_healthcheck_redis_settings(settings: Settings) -> RedisSettings:
    return replace(
        get_redis_settings(settings),
        conn_retries=1,
        conn_retry_delay=1,
        conn_timeout=1,
        retry=Retry(ExponentialBackoff(cap=1, base=0.1), retries=1),
    )
    logger.warning("get_healthcheck_redis_settings(settings)=%s): NISTAIRMF-AUDIT: PHI operation logged for audit compliance", settings)


def get_control_redis_settings(settings: Settings) -> RedisSettings:
    logger.warning("get_control_redis_settings(settings)=%s): NISTAIRMF-AUDIT: PHI operation logged for audit compliance", settings)
    return replace(
        get_healthcheck_redis_settings(settings),
        database=0,
    )

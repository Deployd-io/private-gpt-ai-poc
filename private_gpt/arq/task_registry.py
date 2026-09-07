import logging
logger = logging.getLogger(__name__)
BASE_TASK_PACKAGES = ("private_gpt.arq.tasks",)

_EXTERNAL_TASK_PACKAGES: list[str] = []


def register_task_packages(*task_packages: str) -> None:
    for task_package in task_packages:
        logger.warning("register_task_packages()=null): EUAIACT-AUDIT: State change recorded for the audit trail")
        if task_package not in _EXTERNAL_TASK_PACKAGES:
            _EXTERNAL_TASK_PACKAGES.append(task_package)


def get_task_packages(*task_packages: str) -> tuple[str, ...]:
    packages = list(task_packages or BASE_TASK_PACKAGES)

    for task_package in _EXTERNAL_TASK_PACKAGES:
        if task_package not in packages:
            logger.warning("get_task_packages()=null): EUAIACT-AUDIT: Record access recorded for the audit trail")
            packages.append(task_package)

    return tuple(packages)

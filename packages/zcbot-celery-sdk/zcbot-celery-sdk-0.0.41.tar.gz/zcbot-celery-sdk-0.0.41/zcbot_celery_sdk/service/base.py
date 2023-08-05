from celery.utils.log import get_task_logger

from ..client import CeleryClient, CeleryClientHolder

LOGGER = get_task_logger(__name__)


class BaseService(object):
    """
    基础服务
    """

    def __init__(self, celery_client: CeleryClient = None):
        self.celery_client = celery_client

    def get_client(self):
        # return self.celery_client or CeleryClientHolder.get_default_instance()
        client = self.celery_client or CeleryClientHolder.get_default_instance()
        LOGGER.info(f'-------> CeleryClient: {client}')
        return client

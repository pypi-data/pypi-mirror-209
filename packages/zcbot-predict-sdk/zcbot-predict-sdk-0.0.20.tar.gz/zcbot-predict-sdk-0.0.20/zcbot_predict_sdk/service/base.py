from celery.utils.log import get_task_logger

from ..client import PredictClient, PredictClientHolder

LOGGER = get_task_logger(__name__)


class BaseService(object):
    """
    基础服务
    """

    def __init__(self, celery_client: PredictClient = None):
        self.celery_client = celery_client

    def get_client(self):
        # return self.celery_client or PredictClientHolder.get_default_instance()
        client = self.celery_client or PredictClientHolder.get_default_instance()
        LOGGER.info(f'-------> PredictClient: {client}')
        return client

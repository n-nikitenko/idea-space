import logging

from celery import shared_task
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.utils import aware_utcnow

logger = logging.getLogger('celery')


@shared_task
def clear_blacklist_tokens():
    """"Удаляет устаревшие токены"""

    expired_tokens = OutstandingToken.objects.filter(expires_at__lte=aware_utcnow())
    count = expired_tokens.count()
    expired_tokens.delete()

    logger.info(f"Удалено {count} устаревших токенов.")

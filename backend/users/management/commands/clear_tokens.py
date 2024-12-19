from django.core.management.base import BaseCommand
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.utils import aware_utcnow


class Command(BaseCommand):
    help = "Удаляет устаревшие токены"

    def handle(self, *args, **kwargs):
        # Удаляем все токены, срок действия которых истек
        expired_tokens = OutstandingToken.objects.filter(expires_at__lte=aware_utcnow())
        count = expired_tokens.count()
        expired_tokens.delete()

        self.stdout.write(f"Удалено {count} устаревших токенов.")

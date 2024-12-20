import uuid

from django.conf import settings
from django.db import models

from pages.managers import PageManager


class Page(models.Model):
    """модель страницы"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pages"
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Используем менеджер для обработки логики выборки
    objects = PageManager()

    def __str__(self):
        return self.title

    def get_children(self):
        """Получить дочерние страницы для текущей страницы"""
        return Page.objects.get_children(self)

    def get_full_path(self):
        """Получить полный путь от корня до текущей страницы"""
        return Page.objects.get_full_path(self)

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from pages.apps import PagesConfig
from pages.views import PageViewSet

app_name = PagesConfig.name

# Создаём роутер для PageViewSet
router = SimpleRouter()
pages_prefix = "pages"
router.register(pages_prefix, PageViewSet, basename="pages")

urlpatterns = [
    path("", include(router.urls)),
]

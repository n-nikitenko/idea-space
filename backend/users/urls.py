from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import UserTokenObtainPairView, UserViewSet, UserTokenRefreshView

app_name = UsersConfig.name

router = SimpleRouter()
users_prefix = "users"
router.register(users_prefix, UserViewSet, basename="users")

# Определяем подмаршруты для аутентификации
auth_patterns = [
    path(
        "login/",
        UserTokenObtainPairView.as_view(permission_classes=[AllowAny]),
        name="token_obtain_pair",
    ),  # must be first
    path("token/refresh/", UserTokenRefreshView.as_view(permission_classes=[AllowAny]), name="token_refresh"),
]

urlpatterns = [
    path(f"{users_prefix}/", include(auth_patterns)),
    path("", include(router.urls)),
]

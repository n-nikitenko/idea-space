from django.urls import path, include
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
        UserTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("token/refresh/", UserTokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = [
    path("", include(router.urls)),
    path(f"{users_prefix}/", include(auth_patterns)),
]

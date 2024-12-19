from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import (TokenRefreshSerializer)
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.authentication import BlacklistJWTAuthentication
from users.models import User
from users.serializers import UserSerializer
from users.utils import add_to_blacklist


class UserTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        tags=["Аутентификация"],
        operation_description="Получение токена. Этот эндпоинт позволяет получить JWT токен на "
                              "основе учетных данных пользователя.",
        responses={
            200: openapi.Response("Успех", TokenRefreshSerializer),
            401: "Неверные учетные данные",
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        tags=["Аутентификация"],
        operation_description="Обновление токена. Этот эндпоинт позволяет обновить JWT токен, предоставленный ранее.",
        responses={
            200: openapi.Response("Успех", TokenRefreshSerializer),
            401: "Токен недействителен",
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Получение списка пользователей", tags=["Пользователи"]
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Регистрация пользователя", tags=["Пользователи"]
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Получение данных пользователя по id", tags=["Пользователи"]
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Обновление данных пользователя по id", tags=["Пользователи"]
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Частичное обновление данных пользователя по id", tags=["Пользователи"]
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удаление данных пользователя по id", tags=["Пользователи"]
    ),
)
@method_decorator(
    name="logout",
    decorator=swagger_auto_schema(operation_description="Выход из системы\n", tags=["Аутентификация"], responses={
        205: "Успех",
        401: "Пользователь не авторизован",
        400: "Неверные данные"
    }, ),

)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [BlacklistJWTAuthentication]

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (
                AllowAny,
            )
        else:
            self.permission_classes = (
                IsAuthenticated,
            )
        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_serializer_class(self):
        if self.action == "logout":
            return TokenRefreshSerializer
        else:
            return UserSerializer

    @action(["POST"], url_path=r"logout", url_name="logout", detail=False)
    def logout(self, request):
        """Выход из системы"""
        try:
            access_token = request.headers.get("Authorization").split(" ")[1]

            # Аннулируем access токен
            access = AccessToken(access_token)
            # Добавляем токен в черный список
            add_to_blacklist(str(access))

            # Черный список refresh токена
            token = RefreshToken(request.data["refresh"])
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

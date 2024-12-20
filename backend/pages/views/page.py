from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pages.models import Page
from pages.serializers import PageSerializer
from users.authentication import BlacklistJWTAuthentication


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Получение списка страниц", tags=["Страницы"]
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Создание страницы", tags=["Страницы"]
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Получение данных страницы по id", tags=["Страницы"]
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Обновление данных страницы по id", tags=["Страницы"]
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Частичное обновление данных страницы по id", tags=["Страницы"]
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удаление данных страницы по id", tags=["Страницы"]
    ),
)
@method_decorator(
    name="roots",
    decorator=swagger_auto_schema(
        operation_description="Получение всех корневых страниц", tags=["Страницы"]
    ),
)
class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    authentication_classes = [BlacklistJWTAuthentication]

    # todo: добавить пагинацию для list

    @action(detail=False, methods=['get'])
    def roots(self, request):
        """Получение всех корневых страниц"""

        root_pages = Page.objects.get_root_pages()
        serializer = PageSerializer(root_pages, many=True)
        return Response(serializer.data)

    #
    @action(detail=True, methods=['get'])
    def children(self, request, pk=None):
        """Получение дочерних страниц для конкретной страницы"""

        page = self.get_object()
        children = page.get_children()
        serializer = PageSerializer(children, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def full_path(self, request, pk=None):
        """Получение полного пути страницы"""

        page = self.get_object()
        full_path = page.get_full_path()
        return Response({'full_path': full_path})

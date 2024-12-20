from django.db import models


class PageManager(models.Manager):
    """Менеджер для работы с деревом страниц"""

    def get_root_pages(self):
        """Получить все корневые страницы (не имеющие родителя)"""
        return self.filter(parent=None)

    def get_children(self, page):
        """Получить все дочерние страницы"""
        return self.filter(parent=page)

    def get_full_path(self, page):
        """Получить полный путь страницы от корня до самой страницы"""
        path = [page.title]
        current_page = page.parent
        while current_page:
            path.insert(0, current_page.title)
            current_page = current_page.parent
        return " > ".join(path)

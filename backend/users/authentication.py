from rest_framework_simplejwt.authentication import JWTAuthentication

from config.utils.redis import redis_client


class BlacklistJWTAuthentication(JWTAuthentication):
    """проверка, что access-токен не находится в blacklist"""
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ")[1]

        # Проверяем, есть ли токен в черном списке
        if redis_client.get(token):
            return None

        return super().authenticate(request)

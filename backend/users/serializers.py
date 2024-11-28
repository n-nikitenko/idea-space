from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
        )
        optional_fields = ("first_name", "last_name", "email")
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
        }

from rest_framework import serializers

from pages.models import Page


class PageSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Page.objects.all(), required=False)

    class Meta:
        model = Page
        fields = ['id', 'title', 'owner', 'parent', 'created_at', 'updated_at']
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

from rest_framework import serializers
from apps.user.models.user import User
from apps.base.mixins.generic_mixin import GenericSerializerMixin
from typing import Any, Dict


class UserDetailSerializer(GenericSerializerMixin, serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    id = serializers.UUIDField(read_only=True)

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'id')

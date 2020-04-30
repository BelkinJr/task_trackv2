from rest_framework import serializers
from apps.notes.models.note import Note
from apps.user.serializers.user_detail_serializer import UserDetailSerializer
from apps.user.models.user import User
from typing import Any, Dict
from apps.base.mixins.generic_mixin import GenericSerializerMixin


class NoteCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(pk_field=serializers.UUIDField(source='id'), queryset=User.objects.all())

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    class Meta:
        model = Note
        fields = ('author', 'body', 'id')

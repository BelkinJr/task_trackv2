from rest_framework import serializers
from apps.notes.models.note import Note
from typing import Any, Dict
from apps.base.mixins.generic_mixin import GenericSerializerMixin


class NoteCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    class Meta:
        model = Note
        fields = ('author', 'body', 'id')

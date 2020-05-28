from rest_framework import serializers
from apps.notes.models.note import Note
from typing import Any, Dict
from apps.user.models.user import User
from apps.base.mixins.generic_mixin import GenericSerializerMixin


class NoteCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    def validate(self, attrs: Dict[str, Any]):
        user_id = attrs['author']
        user = User.objects.get(id=user_id)
        team_id = attrs['team']
        if user.teams.filter(id=team_id).exists():
            return True
        else:
            print("User is not in the team")
            return False

    class Meta:
        model = Note
        fields = ('author', 'body', 'team')

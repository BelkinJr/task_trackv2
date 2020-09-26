from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.notes.models.note import Note
from typing import Any, Dict

from apps.team.models.team import Team
from apps.user.models.user import User
from apps.base.mixins.generic_mixin import GenericSerializerMixin


class NoteCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('body', 'team')

    def __init__(self, user: User, *args: Any, **kwargs: Any):
        assert isinstance(user, User), f"{user} is given"
        self._user = user
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    def validate_team(self, value: str) -> str:
        try:
            team_obj = Team.objects.get(id=value)
        except Team.DoesNotExist:
            raise ValidationError("Team does not exist")

        if not self._user.teams.filter(id=team_obj.id).exists():
            raise ValidationError("User is not in the team")

        return value

    def create(self, validated_data: Dict[str, Any]) -> Note:
        validated_data.update({"author": self._user})
        return super().create(validated_data)

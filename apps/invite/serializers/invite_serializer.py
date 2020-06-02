from rest_framework import serializers
from apps.invite.models.invite import Invite
from apps.base.mixins.generic_mixin import GenericSerializerMixin
from apps.user.models.user import User
from apps.team.models.team import Team
from typing import Any, Dict


class InviteCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ('user', )

    def __init__(self, team: Team, **kwargs):
        self._team = team
        super().__init__(self, **kwargs)

    def create(self, validated_data):
        data = {'user': validated_data.get('user'),
                'team': self._team}
        super().create(data)

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        team = self._team
        user = attrs.get('user')  # TODO: to be fixed
        if team in user.teams.all():
            raise serializers.ValidationError("User is already in the team")
        else:
            return attrs

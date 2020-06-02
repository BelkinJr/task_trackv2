from rest_framework import serializers
from apps.invite.models.invite import Invite
from apps.base.mixins.generic_mixin import GenericSerializerMixin
from apps.user.models.user import User
from apps.team.models.team import Team
from typing import Any, Dict


class InviteCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):

    def __init__(self, team: Team, **kwargs):
        self._team = team
        super().__init__(self, **kwargs)

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        team = attrs.get('team')
        user = User.objects.get(id=attrs['id'])  # TODO: to be fixed
        if team in user.teams.all():
            raise serializers.ValidationError("User is already in the team")
        else:
            attrs.update({'user': user.id})
            return attrs

    class Meta:
        model = Invite
        fields = ('user', 'team', )

from rest_framework import serializers
from apps.invite.models.invite import Invite
from apps.base.mixins.generic_mixin import GenericSerializerMixin
from typing import Any, Dict


class InviteCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    def validate_user(self, attrs: Dict[str, Any]):
        team = attrs['team']
        user = attrs['user']
        if team in user.teams.all():
            print("User is already in the team")
            return False
        else:
            return True

    class Meta:
        model = Invite
        fields = ('user', 'team', )

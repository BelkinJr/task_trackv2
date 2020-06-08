from rest_framework import serializers
from apps.base.mixins.generic_mixin import GenericSerializerMixin
from apps.user.models.user import User
from django.utils import timezone
from apps.base.constants import JWT_EXP_INVITE_SECONDS
from apps.invite.utils.create_invite_token import create_invite_token
import datetime
from apps.team.models.team import Team
from apps.invite.models.invite_user_to_team import InviteUserToTeam
from typing import Any, Dict


class InviteCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = InviteUserToTeam
        fields = ('user', )

    def __init__(self, team: Team, **kwargs):
        self._team = team
        super().__init__(**kwargs)

    def create(self, validated_data):
        data = {'user': validated_data.get('user'),
                'team': self._team,
                'token_date_expired': int(
            datetime.datetime.now(timezone.get_default_timezone()).timestamp()) + JWT_EXP_INVITE_SECONDS}
        return self.create_invite(data)

    def create_invite(self, data):
        invite = InviteUserToTeam.objects.create(**data)
        token = create_invite_token(invite.id)
        invite.token = token
        invite.save()
        return invite

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        team = self._team
        user = attrs.get('user')  # TODO: to be fixed
        user_obj = User.objects.get(id=user)
        if team in user_obj.teams.all():
            raise serializers.ValidationError("User is already in the team")
        if not InviteUserToTeam.objects.filter(team=team, user=user, status='PEN').exists():
            raise serializers.ValidationError("Invite has already been issued")
        else:
            return attrs

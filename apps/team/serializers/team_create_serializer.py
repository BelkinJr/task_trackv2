from rest_framework import serializers
from apps.team.models import Team, UserTeam
from apps.user.models import User
from apps.user.serializers.user_detail_serializer import UserDetailSerializer
from apps.team.serializers.user_team_serializer import UserTeamSerializer
from typing import Any, Dict
from apps.base.mixins.generic_mixin import GenericSerializerMixin


class TeamCreateSerializer(GenericSerializerMixin, serializers.ModelSerializer):

    def to_internal_value(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().to_internal_value(self.transform_input(data))
        return data

    def create(self, validated_data: Dict[str, Any]) -> Team:
        team = super().create(validated_data)
        user = User.objects.get(id=team.creator_id)
        team.users.add(user)
        return team

    class Meta:
        model = Team
        fields = ['team_name', 'users', 'id', 'creator_id', ]

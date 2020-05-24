from rest_framework import serializers
from apps.team.models import UserTeam


class UserTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTeam
        fields = ('team', 'user',)

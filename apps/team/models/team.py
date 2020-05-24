from django.db import models
from apps.base.models.base import BaseModel
from apps.team.models.user_team import UserTeam
from apps.user.models import User


class Team (BaseModel):

    team_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='teams', through=UserTeam)
    creator_id = models.UUIDField()

    class Meta:
        db_table = 'team'
        verbose_name = "team"

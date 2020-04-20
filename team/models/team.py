from django.db import models
from base.models import BaseModel
from user.models import User
from team.models.userteam import UserTeamRelation


class Team (BaseModel):

    team_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='teams', through=UserTeamRelation)

    class Meta:
        db_table = 'team_table'
        verbose_name = "Teams"

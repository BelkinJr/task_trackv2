from django.db import models
from base.models import BaseModel
from user.models import User
from team.models.userteam import UserTeamRelation

# Create your models here.

class Team (BaseModel):

    team_name = models.CharField(max_length=255)
    uesr_count = models.IntegerField()
    users = models.ManyToManyField(User, related_name='teams', through=UserTeamRelation)

    class Meta:
        db_table = 'team_table'
        verbose_name = "Teams"
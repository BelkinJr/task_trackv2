from django.db import models
from base.models import BaseModel
from user.models import User


class UserTeamRelation (BaseModel):

    team = models.ForeignKey('Team', related_name='team_users',  on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_teams', on_delete=models.CASCADE)

    class Meta:
        db_table = 'UserTeamRelation_table'
        verbose_name = "User Team"

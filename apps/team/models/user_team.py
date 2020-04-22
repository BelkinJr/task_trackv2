from django.db import models
from apps.base.models import BaseModel
from apps.user.models import User


class UserTeam(BaseModel):

    team = models.ForeignKey('Team', related_name='team_users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_teams', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_team'
        verbose_name = "user team"

from django.db import models
from apps.base.models import BaseModel
from apps.user.models import User
from apps.team.models import Team


class Note(BaseModel):

    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='notes')
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='notes', null=False)

    class Meta:
        db_table = 'note'
        verbose_name = 'note'

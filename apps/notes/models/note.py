from django.db import models
from apps.base.models import BaseModel
from apps.user.models import User


class Note(BaseModel):

    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        db_table = 'note'
        verbose_name = 'note'

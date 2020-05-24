from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.base.managers import IsActiveManager, AllObjectsManager
import uuid


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    username = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    objects = IsActiveManager
    objects_all = AllObjectsManager

    USERNAME_FIELD = 'username'

    def delete(self, using=None, keep_parents=False):
        self.is_active = False

    class Meta:
        db_table = 'user'
        verbose_name = 'user'

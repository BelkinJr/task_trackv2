from django.db import models
from apps.base.managers import IsActiveManager, AllObjectsManager
import uuid


class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    objects = IsActiveManager
    objects_all = AllObjectsManager

    def delete(self, using=None, keep_parents=False):
        self.is_active = False

    class Meta:
        abstract = True

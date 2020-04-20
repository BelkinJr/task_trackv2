from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = date_modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta: 
        abstract = True
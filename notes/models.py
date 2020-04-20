from django.db import models
from base.models import BaseModel
from user.models import User

# Create your models here.

class Note (BaseModel):
    
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        ordering = ('-date_created',)
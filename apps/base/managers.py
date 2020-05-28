from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class CustomBaseQuerySet(models.QuerySet):
    def delete(self):
        self.update(is_active=False)


class IsActiveManager(models.Manager):
    def get_queryset(self):
        return CustomBaseQuerySet(self.model, using=self._db).filter(is_active=True)


class IsActiveUserManager(BaseUserManager):
    def get_queryset(self):
        return CustomBaseQuerySet(self.model, using=self._db).filter(is_active=True)


class AllObjectsManager(models.Manager):
    def get_queryset(self):
        return CustomBaseQuerySet(self.model, using=self._db)


class AllObjectsUserManager(BaseUserManager):
    def get_queryset(self):
        return CustomBaseQuerySet(self.model, using=self._db)

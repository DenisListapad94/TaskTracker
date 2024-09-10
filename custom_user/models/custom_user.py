from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from custom_user.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()

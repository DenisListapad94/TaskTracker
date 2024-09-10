from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from custom_user.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(null=True)
    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

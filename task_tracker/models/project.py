from django.db import models

from base.models import BaseModel


class Project(BaseModel,models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "project"
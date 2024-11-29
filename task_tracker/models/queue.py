from django.db import models

from base.models import BaseModel


class TaskQueue(BaseModel, models.Model):
    value = models.IntegerField()

    class Meta:
        db_table = "task_queue"

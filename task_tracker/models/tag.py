from django.db import models

from base.models import BaseModel


class Tag(BaseModel,models.Model):
    name = models.CharField(max_length=64)
    tasks = models.ManyToManyField(
        to="Task",
        related_name="tags"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tag"
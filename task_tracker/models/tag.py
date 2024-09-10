from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(
        to="Task",
        related_name="tags"
    )

    def __str__(self):
        return self.name
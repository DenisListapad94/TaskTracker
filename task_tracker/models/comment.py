from django.db import models

from custom_user.models import CustomUser


class Comment(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(
        to="Task",
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
    )
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
    )

    def __str__(self):
        return self.title

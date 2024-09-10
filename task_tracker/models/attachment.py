from django.db import models

from custom_user.models import CustomUser


class Attachment(models.Model):
    file_name = models.CharField(max_length=64, null=True)
    file = models.FileField(null=True)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="attachments",
        null=True,
    )
    task = models.ForeignKey(
        to="Task",
        on_delete=models.CASCADE,
        related_name="attachments",
        null=True
    )

    def __str__(self):
        return self.file_name

from django.db import models
from custom_user.models import CustomUser

STATUS_CHOICES = [
    ("op", "Open"),
    ("cl", "Close"),
    ("pr", "Process"),
]
PRIORITY_CHOICES = [
    ("h", "High"),
    ("m", "Medium"),
    ("l", "Low"),
]


class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, null=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=2, null=True)
    height_level = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(
        to="Project",
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True
    )
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True
    )

    def __str__(self):
        return self.title

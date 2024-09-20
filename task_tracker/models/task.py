from django.db import models

from base.models import BaseModel
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


class Task(BaseModel,models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='заголовок'
    )
    description = models.CharField(
        max_length=256,
        verbose_name='описание'
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=2,
        null=True,
        verbose_name='статус'
    )
    priority = models.CharField(
        choices=PRIORITY_CHOICES,
        max_length=2,
        null=True,
        verbose_name='приоритет'
    )
    height_level = models.PositiveIntegerField(
        null=True,
        verbose_name='уровень сложности'
    )

    project = models.ForeignKey(
        to="Project",
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        verbose_name="проект"
    )
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        verbose_name="пользователь"
    )
    photo = models.ImageField(
        upload_to="tasks",
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'задачи'
        verbose_name_plural = 'задачи'
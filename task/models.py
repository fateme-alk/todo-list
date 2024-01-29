# Create your models here.
from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("high", "high"),
        ("medium", "medium"),
        ("low", "low"),
    )

    title = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title.title()

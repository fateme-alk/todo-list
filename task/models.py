# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("high", "high"),
        ("medium", "medium"),
        ("low", "low"),
    )

    doer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=False)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    status = models.BooleanField()

    def __str__(self):
        return self.title.title()

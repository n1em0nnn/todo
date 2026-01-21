from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    class Status(models.TextChoices):
        NEW = "new", "NEW"
        DONE = "done", "DONE"
        ARCHIVED = "archived", "ARCHIVED"
    title = models.CharField(max_length=100)
    descr = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    def __str__(self):
        return self.title
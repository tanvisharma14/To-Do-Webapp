from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250)
    isCompleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.task

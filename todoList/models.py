from django.db import models


# Create your models here.
class List(models.Model):
    task = models.CharField(max_length=200)
    time_task_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    time_task_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.task

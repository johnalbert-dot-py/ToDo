from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    shift = models.CharField(choices=(("PM", "PM"), ("AM", "AM")), null=True, blank=True, max_length=5)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Habit(models.Model):
    title = models.CharField(max_length=15)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    high_priority = models.BooleanField(default=False)

    def __str__(self):
        return self.title
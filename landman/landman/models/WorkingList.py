from django.contrib.auth.models import User
from django.db import models

from landman.models.Agreement import Agreement

class WorkingList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    agreements = models.ManyToManyField(Agreement, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.agreements.count()})"
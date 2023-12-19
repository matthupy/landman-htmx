from django.contrib.auth.models import User
from django.db import models

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField()

    def __str__(self):
        return f"ID # {self.id} ({self.update_user}, {self.update_date})"
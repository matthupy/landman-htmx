from django.contrib.auth.models import User
from django.db import models

from landman.models.State import State

class County(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    update_date = models.DateField()
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "County"
        verbose_name_plural = "Counties"
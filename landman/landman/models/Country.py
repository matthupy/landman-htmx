from django.contrib.auth.models import User
from django.db import models

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=4)
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    update_date = models.DateField()
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.abbreviation} | {self.name}"
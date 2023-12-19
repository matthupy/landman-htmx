from django.contrib.auth.models import User
from django.db import models

from landman.models.Country import Country
from landman.models.SurveyType import SurveyType

class State(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    code = models.CharField(max_length=6)
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    survey = models.ForeignKey(SurveyType, on_delete=models.PROTECT)
    update_date = models.DateField()
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.abbreviation} | {self.name}"
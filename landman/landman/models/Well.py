from django.db import models
from simple_history.models import HistoricalRecords

from landman.models.WellStatus import WellStatus

class Well(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    status = models.ForeignKey(WellStatus, on_delete=models.PROTECT)
    latitude = models.DecimalField(decimal_places=15, max_digits= 18, default=0)
    longitude = models.DecimalField(decimal_places=15, max_digits= 18, default=0)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name} ({self.status.description})"
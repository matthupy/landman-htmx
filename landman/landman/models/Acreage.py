from django.db import models
from simple_history.models import HistoricalRecords

from landman.models.AcreageType import AcreageType
from landman.models.Agreement import Agreement
from landman.models.Unit import Unit

class Acreage(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(AcreageType, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, related_name='acreage', blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.agreement.number} - {self.type.description} - {self.amount} {self.unit.description}"
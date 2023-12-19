from django.db import models

from landman.models.Address import Address
from landman.models.BackupWithholdingType import BackupWithholdingType
from landman.models.EntityType import EntityType

class Landowner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    entity_type = models.ForeignKey(EntityType, on_delete=models.PROTECT)
    address = models.ManyToManyField(Address)
    email = models.EmailField(max_length=254)
    ssn = models.CharField(max_length=11, blank=False, verbose_name="Social Security Number")
    backupWithholdingType = models.ForeignKey(BackupWithholdingType, on_delete=models.PROTECT)
    backupWithholding = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}"
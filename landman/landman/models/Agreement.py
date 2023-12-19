from django.db import models
from simple_history.models import HistoricalRecords

from landman.models.AgreementStage import AgreementStage
from landman.models.AgreementStatus import AgreementStatus
from landman.models.AgreementType import AgreementType
from landman.models.LandDivision import LandDivision
from landman.models.Right import Right
from landman.models.Well import Well

class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    number = models.CharField(max_length=40)
    type = models.ForeignKey(AgreementType, on_delete=models.PROTECT)
    status = models.ForeignKey(AgreementStatus, on_delete=models.PROTECT)
    stage = models.ForeignKey(AgreementStage, on_delete=models.PROTECT)
    landDivision = models.ForeignKey(LandDivision, on_delete=models.PROTECT)
    originalLessee = models.CharField(max_length=40)
    agreementDate = models.DateField()
    effectiveDate = models.DateField()
    term = models.IntegerField(null=False)
    rights = models.ForeignKey(Right, on_delete=models.PROTECT)
    related = models.ManyToManyField('self', blank=True)
    wells = models.ManyToManyField(Well, blank=True)
    history = HistoricalRecords()

    def inactivate(self):
        from landman.models import AgreementStatus
        if (self.status == AgreementStatus.objects.filter(code="IN").first()):
            return False
        else:
            self.status = AgreementStatus.objects.filter(code="IN").first()
            self.save()

    def reactivate(self):
        from landman.models import AgreementStatus
        if (self.status == AgreementStatus.objects.filter(code="A").first()):
            return False
        else:
            self.status = AgreementStatus.objects.filter(code="A").first()
            self.save()

    def __str__(self):
        return f"{self.number} - {self.name}"
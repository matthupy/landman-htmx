from django.db import models

from landman.models.Agreement import Agreement
from landman.models.SurveyType import SurveyType

class LegalSegment(models.Model):
    id = models.AutoField(primary_key=True)
    agreement = models.ForeignKey(Agreement, related_name='legal_segments', on_delete=models.PROTECT)
    surveyType = models.ForeignKey(SurveyType, on_delete=models.PROTECT)
    acreage = models.DecimalField(decimal_places=6, max_digits=13, blank=True, null=True)

    class Meta:
        abstract = True
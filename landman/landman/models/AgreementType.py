from django.db import models

from landman.models.SubjectType import SubjectType

class AgreementType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    category = models.ForeignKey(SubjectType, on_delete=models.PROTECT, related_name='agreement_types')
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.category.code}-{self.code} : {self.description}"

    class Meta:
        verbose_name = "Agreement Type"
        verbose_name_plural = "Agreement Types"
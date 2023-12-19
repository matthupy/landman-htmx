from django.db import models

class BusinessAssociateType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Business Associate Type"
        verbose_name_plural = "Business Associate Types"

    def __str__(self):
        return f"{self.code} | {self.description}"
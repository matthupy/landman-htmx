from django.db import models

class BackupWithholdingType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Backup Withholding Type"
        verbose_name_plural = "Backup Withholding Types"

    def __str__(self):
        return f"{self.code} | {self.description}"
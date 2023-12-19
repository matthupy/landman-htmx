from django.db import models

class AgreementStage(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=128)
    index = models.IntegerField(unique=True)

    class Meta:
        verbose_name = "Agreement Stage"
        verbose_name_plural = "Agreement Stages"

    def __str__(self):
        return f"{self.code} | {self.description} ({self.index})"
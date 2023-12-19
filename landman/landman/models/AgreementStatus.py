from django.db import models

class AgreementStatus(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.code} : {self.description}"

    class Meta:
        verbose_name = "Agreement Status"
        verbose_name_plural = "Agreement Statuses"
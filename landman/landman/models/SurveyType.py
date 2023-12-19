from django.db import models

class SurveyType(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Survey Type"
        verbose_name_plural = "Survey Types"

    def __str__(self):
        return f"{self.description}"
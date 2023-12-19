from django.db import models

class WellStatus(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Well Status"
        verbose_name_plural = "Well Statuses"
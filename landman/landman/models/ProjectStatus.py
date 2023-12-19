from django.db import models

class ProjectStatus(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Project Status"
        verbose_name_plural = "Project Statuses"

    def __str__(self):
        return f"{self.code} | {self.description}"
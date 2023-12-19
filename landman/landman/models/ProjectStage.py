from django.db import models

class ProjectStage(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=128)
    index = models.IntegerField(unique=True)

    class Meta:
        verbose_name = "Project Stage"
        verbose_name_plural = "Project Stages"

    def __str__(self):
        return f"{self.code} | {self.description} ({self.index})"
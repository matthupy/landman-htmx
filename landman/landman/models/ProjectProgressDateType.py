from django.db import models

class ProjectProgressDateType(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Project Progress Date Type"
        verbose_name_plural = "Project Progress Date Types"

    def __str__(self):
        return f"{self.description}"
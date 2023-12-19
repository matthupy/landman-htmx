from django.db import models

class TaskType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Task Type"
        verbose_name_plural = "Task Types"

    def __str__(self):
        return f"{self.code} | {self.description}"
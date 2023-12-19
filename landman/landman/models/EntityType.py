from django.db import models

class EntityType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Entity Type"
        verbose_name_plural = "Entity Types"

    def __str__(self):
        return f"{self.code} | {self.description}"
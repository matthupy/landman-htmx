from django.core.exceptions import ValidationError
from django.db import models
from simple_history.models import HistoricalRecords

from landman.models.TaskStatus import TaskStatus
from landman.models.TaskType import TaskType

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    type = models.ForeignKey(TaskType, on_delete=models.PROTECT)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    effDateFrom = models.DateField(verbose_name="Effective Date From", blank=True)
    effDateTo = models.DateField(verbose_name="Effective Date To", blank=True)
    dueDate = models.DateField(verbose_name="Due Date", blank=True)
    history = HistoricalRecords()

    def validate_effective_dates(self):
        """
            Validates that the effective date to is greater than the effective date from
        """
        print('into task validation')
        print('validation should be {0}'.format(self.effDateFrom <= self.effDateTo))
        if (self.effDateFrom <= self.effDateTo):
            return True
        else: return False

    def clean(self):
        # Make sure that the effective date to is after effective date from
        test_result = self.effDateFrom <= self.effDateTo
        if (not test_result):
            raise ValidationError('Effective Date To cannot be before or equal to Effective Date From')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs) # Call the real save event

    def __str__(self):
        return f"{self.name} ({self.status})"
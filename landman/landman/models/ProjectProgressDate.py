from django.contrib.auth.models import User
from django.db import models

from landman.models.ProjectProgressDateStatus import ProjectProgressDateStatus
from landman.models.ProjectProgressDateType import ProjectProgressDateType

class ProjectProgressDate(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(ProjectProgressDateType, on_delete=models.PROTECT)
    status = models.ForeignKey(ProjectProgressDateStatus, on_delete=models.PROTECT)
    due_date = models.DateField(verbose_name="Due Date")
    completed_date = models.DateField(verbose_name="Completed Date")
    assigned_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name="assigned_to")
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="update_user")
    update_date = models.DateTimeField()
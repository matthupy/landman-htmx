from django.db import models
from simple_history.models import HistoricalRecords

from landman.models.Country import Country
from landman.models.County import County
from landman.models.Landowner import Landowner
from landman.models.ProjectProgressDate import ProjectProgressDate
from landman.models.ProjectStage import ProjectStage
from landman.models.ProjectStatus import ProjectStatus
from landman.models.ProjectType import ProjectType
from landman.models.State import State
from landman.models.Task import Task


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    description = models.TextField()
    type = models.ForeignKey(ProjectType, on_delete=models.PROTECT)
    status = models.ForeignKey(ProjectStatus, on_delete=models.PROTECT)
    stage = models.ForeignKey(ProjectStage, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    county = models.ForeignKey(County, on_delete=models.PROTECT)
    tasks = models.ManyToManyField(Task, blank=True)
    contacts = models.ManyToManyField(Landowner, blank=True)
    cross_references = models.ManyToManyField('self', blank=True)
    progress_dates = models.ManyToManyField(ProjectProgressDate, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.id} - {self.name}"
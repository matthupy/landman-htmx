# imports
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from landman.models import (
    Acreage,
    AcreageType,
    Address,
    Agreement,
    AgreementStage,
    AgreementStatus,
    AgreementType,
    BackupWithholdingType,
    BusinessAssociateType,
    Country,
    County,
    EntityType,
    JeffersonianLegalHeader,
    LandDivision,
    Landowner,
    Note,
    Project,
    ProjectProgressDate,
    ProjectProgressDateStatus,
    ProjectProgressDateType,
    ProjectStage,
    ProjectStatus,
    ProjectType,
    Right,
    State,
    SubjectType,
    SurveyType,
    Task,
    TaskType,
    TaskStatus,
    Unit,
    Well,
    WellStatus,
    Well,
    WorkingList
)

from .AgreementHistoryAdmin import AgreementHistoryAdmin
from .CountryAdmin import CountryAdmin
from .CountyAdmin import CountyAdmin
from .JeffersonianLegalHeaderAdmin import JeffersonianLegalHeaderHistoryAdmin
from .StateAdmin import StateAdmin
from .TaskAdmin import TaskHistoryAdmin

## CODE TABLES
admin.site.register(Acreage)
admin.site.register(AcreageType)
admin.site.register(Address)
admin.site.register(AgreementStage)
admin.site.register(AgreementStatus)
admin.site.register(AgreementType)
admin.site.register(BackupWithholdingType)
admin.site.register(BusinessAssociateType)
admin.site.register(EntityType)
admin.site.register(LandDivision)
admin.site.register(Landowner)
admin.site.register(Note)
admin.site.register(Project)
admin.site.register(ProjectProgressDate)
admin.site.register(ProjectProgressDateStatus)
admin.site.register(ProjectProgressDateType)
admin.site.register(ProjectStage)
admin.site.register(ProjectStatus)
admin.site.register(ProjectType)
admin.site.register(Right)
admin.site.register(SubjectType)
admin.site.register(SurveyType)
admin.site.register(TaskType)
admin.site.register(TaskStatus)
admin.site.register(Unit)
admin.site.register(WellStatus)
admin.site.register(Well, SimpleHistoryAdmin)
admin.site.register(WorkingList)

admin.site.register(Agreement, AgreementHistoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(JeffersonianLegalHeader, JeffersonianLegalHeaderHistoryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Task, TaskHistoryAdmin)
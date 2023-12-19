from simple_history.admin import SimpleHistoryAdmin
from landman.models import *

class TaskHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("id","name","task_type","task_status","effDateFrom","effDateTo","dueDate")
    list_filter = ("type","status")
    search_fields = ("id","name__contains")

    def task_status(self,obj):
        return obj.status.description

    def task_type(self,obj):
        return obj.type.description
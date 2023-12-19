from simple_history.admin import SimpleHistoryAdmin
from landman.models import AgreementStatus, AgreementType, Right

class AgreementHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("number","name","agreement_status","agreement_type","agreement_rights","well_count")
    list_filter = ("status","type","rights")
    search_fields  = ("number__contains","name__contains")

    def agreement_status(self, obj):
        status = AgreementStatus.objects.get(code=obj.status.code)
        return status.description

    def agreement_type(self,obj):
        type = AgreementType.objects.get(code=obj.type.code)
        return type.description

    def agreement_rights(self,obj):
        rights = Right.objects.get(code=obj.rights.code)
        return rights.description

    def well_count(self, obj):
        return obj.wells.count()
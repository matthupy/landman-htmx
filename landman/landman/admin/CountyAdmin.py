from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

class CountyAdmin(admin.ModelAdmin):
    list_display = ("id","country_name","state_code","state_name","code","name","hidden")
    search_fields = ("id","name__contains","code__contains")
    list_filter = (("state__country", RelatedDropdownFilter),
                   ("state", RelatedDropdownFilter),
                    "hidden")
    ordering = ["state","name"]

    def country_name(self,obj):
        return obj.state.country.name

    def state_name(self,obj):
        return obj.state.name

    def state_code(self,obj):
        return obj.state.code
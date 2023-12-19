from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

class StateAdmin(admin.ModelAdmin):
    ## Actions
    def make_hidden(self, request, queryset):
        queryset.update(hidden=True)
    make_hidden.short_description = 'Hide selected states'

    def make_unhidden(self, request, queryset):
        queryset.update(hidden=False)
    make_unhidden.short_description = 'Un-Hide selected states'

    list_display = ("id","country_name","code","abbreviation","name","hidden","county_count")
    search_fields = ("abbreviation__contains","name__contains","code")
    list_filter = (("country", RelatedDropdownFilter),
                   ("survey", RelatedDropdownFilter),
                    "hidden")
    ordering = ["country","abbreviation"]
    actions = [make_hidden, make_unhidden]

    def country_name(self,obj):
        return obj.country.name

    def county_count(self,obj):
        return obj.county_set.all().count()
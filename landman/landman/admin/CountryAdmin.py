from django.contrib import admin
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter


class CountryAdmin(admin.ModelAdmin):
    ## Actions
    def make_hidden(self, request, queryset):
        queryset.update(hidden=True)
    make_hidden.short_description = 'Hide selected countries'

    def make_unhidden(self, request, queryset):
        queryset.update(hidden=False)
    make_unhidden.short_description = 'Un-Hide selected countries'

    list_display = ("id","code","abbreviation","name","hidden","state_count")
    search_fields = ("abbreviation__contains","name__contains")
    list_filter = (("name", ChoiceDropdownFilter),
                    "hidden")
    ordering = ['abbreviation']
    actions = [make_hidden, make_unhidden]

    def state_count(self,obj):
        return obj.state_set.all().count()
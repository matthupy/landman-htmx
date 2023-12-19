from django import forms
from simple_history.admin import SimpleHistoryAdmin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from landman.models import Country, JeffersonianLegalHeader

class JeffersonianLegalHeaderForm(forms.ModelForm):
    class Meta:
        model = JeffersonianLegalHeader
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(JeffersonianLegalHeaderForm, self).__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.filter(hidden=False)

class JeffersonianLegalHeaderHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("id","agreement_number","country_name","state_name","county_name","township_num", "townshipDir", "range_num", "rangeDir", "section_num", "acreage")
    search_fields = ("id","agreement__name__contains","agreement__number__contains")
    list_filter = (("country", RelatedDropdownFilter),
                   ("state", RelatedDropdownFilter),
                   ("county", RelatedDropdownFilter))
    ordering = ["country","state","county", "townshipDir","townshipNum","rangeDir","rangeNum","section"]

    form = JeffersonianLegalHeaderForm

    def agreement_number(self,obj):
        return obj.agreement.number

    def agreement_name(self,obj):
        return obj.agreement.name

    def country_name(self,obj):
        return obj.country.name

    def state_name(self,obj):
        return obj.state.name

    def county_name(self,obj):
        return obj.county.name

    def township_num(self,obj):
        return '{:03}'.format(obj.townshipNum)

    def range_num(self,obj):
        return '{:03}'.format(obj.rangeNum)

    def section_num(self,obj):
        return '{:03}'.format(obj.section)
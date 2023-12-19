from django.db import models
from simple_history.models import HistoricalRecords
from smart_selects.db_fields import ChainedForeignKey

from landman.models.Country import Country
from landman.models.County import County
from landman.models.LegalSegment import LegalSegment
from landman.models.State import State

class JeffersonianLegalHeader(LegalSegment):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    state = ChainedForeignKey(State
                                    , chained_field="country"
                                    , chained_model_field="country"
                                    , show_all=False
                                    , auto_choose=True
                                    , on_delete=models.PROTECT)
    county = ChainedForeignKey(County
                                    , chained_field="state"
                                    , chained_model_field="state"
                                    , show_all=False
                                    , auto_choose=True
                                    , on_delete=models.PROTECT)
    townshipNum = models.IntegerField(blank=False)
    townshipDir = models.CharField(max_length=10, choices=[('N','North'),('S','South')], blank=False, default='N')
    rangeNum = models.IntegerField(blank=False)
    rangeDir = models.CharField(max_length=10, choices=[('E','East'),('W','West')], blank=False, default='E')
    section = models.IntegerField(blank=False)
    history = HistoricalRecords()

    def validate_country_state_county(self):
        """
            Validates that the Country/State/County configuration is valid, meaning the selected county
            is tied to the selected state, and the selected state is tied to the selected country
        """
        if (self.county.state == self.state and self.state.country == self.country):
            return True
        else: return False

    def __str__(self):
        township = 'T' + ('{:03}'.format(self.townshipNum)) + self.townshipDir
        range = 'R' + ('{:03}'.format(self.rangeNum)) + self.rangeDir
        section = 'S' + ('{:03}'.format(self.section))
        return f"ID #{self.id}: {self.country.code} / {self.state.abbreviation} / {self.county.name} / {township} / {range} / {section}"

    def save(self, *args, **kwargs):
        if (self.validate_country_state_county()):
            super().save(*args, **kwargs) # Call the real save event

    class Meta:
        verbose_name = "Jeffersonian Legal Segment"
        verbose_name_plural = "Jeffersonian Legal Segments"
from django.db import models

from landman.models.State import State

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    attention_line1 = models.CharField(max_length=128, blank=True)
    attention_line2 = models.CharField(max_length=128, blank=True)
    address_line1 = models.CharField(max_length=128)
    address_line2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    zip = models.CharField(max_length=5)

    def __str__(self):
        rtn = ""
        if (self.attention_line1):
            rtn = f"{rtn}ATTN: {self.attention_line1}"
        if (self.attention_line2):
            rtn = f"{rtn} {self.attention_line2}"
        if (self.address_line1):
            rtn = f"{rtn} {self.address_line1}"
        if (self.address_line2):
            rtn = f"{rtn} {self.address_line2}"
        if (self.city):
            rtn = f"{rtn} {self.city}"
        if (self.state):
            rtn = f"{rtn}, {self.state.abbreviation}"
        if (self.zip):
            rtn = f"{rtn} {self.zip}"
        return rtn
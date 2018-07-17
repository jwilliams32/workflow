from django import forms
from . import models

class CreateWorkUp(forms.ModelForm):
    class Meta:
        model = models.WorkUp
        fields = ['workup_name', 'workup_instruction','doctor']

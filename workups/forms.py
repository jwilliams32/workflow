from django import forms
from . import models

class CreateWorkup(forms.ModelForm):
    class Meta:
        model = models.Workup
        fields = ['workup_name', 'workup_instruction','doctor','test']

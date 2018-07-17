from django import forms
from . import models

class CreateWorkUp(forms.ModelForm):
    class Meta:
        model = models.WorkUp
        fields = ['work_up_name', 'work_up_instruction','doctor']

from django import forms
from . import models

class CreateTest(forms.ModelForm):
    class Meta:
        model = models.Test
        fields = ['test_name', 'test_description']

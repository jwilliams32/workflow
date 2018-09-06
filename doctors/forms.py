from django import forms
from . import models


class ImageUploadForm(forms.Form):
#     """Image upload form."""
    image = forms.ImageField()

class CreateDoctor(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['doctors_name', 'clinic_type', 'description','doctors_pic']

# class EditDoctor(forms.ModelForm):
#     d
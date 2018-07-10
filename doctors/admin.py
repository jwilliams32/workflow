from django.contrib import admin
from .models import Doctor
from django import forms
from django.forms import Textarea, TextInput
# Register your models here.


# class DoctorForm(forms.ModelForm):
#     description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
#     class Meta:
#         model = Doctor
#
#
# class DoctorAdmin(admin.ModelAdmin):
#     form = DoctorForm


admin.site.register(Doctor)

from django.db import models

# Create your models here.

class Doctor(models.Models):
    doctor = models.TextField(max_length=500)
    clinic = models.TextField(max_length=75)


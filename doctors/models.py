from django.db import models
from django.urls import reverse
# from tests.models import Test
# Create your models here.

class Doctor(models.Model):
    doctors_name = models.CharField(max_length=500)
    clinic_type = models.CharField(max_length=75)
    description = models.TextField(max_length=1000)
    bio = models.CharField(max_length=500, blank=True)
    doctor_pic = models.ImageField(blank=True, null=True,
        upload_to="doctors/%Y/%m/%D/")


    # test = models.ManyToManyField('tests.Test', related_name='doctor_tests')

    def __str__(self):
        return '{0}'.format(self.doctors_name)

    def get_absolute_url(self):
        """
        Returns the url to access the doctors view.
        """

        return reverse('view_doctor', args=[str(self.id)])
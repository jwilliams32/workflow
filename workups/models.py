from django.db import models
# from doctors.models import Doctor
# from ..doctors.models import Doctor
from django.urls import reverse
# Create your models here.

class Workup(models.Model):

    doctor = models.ManyToManyField('doctors.Doctor', related_name='workupdoctors', blank=True)
    test = models.ManyToManyField('tests.Test', related_name='workuptests', blank=True)
    workup_name = models.TextField(max_length=100)
    workup_instruction = models.TextField(max_length=5000)
    upload_file = models.FileField(blank=True, null=True,
       upload_to='uploaded_files/%Y/%m/%D/')

    def __str__(self):
        return '{0}'.format(self.workup_name)

    def get_absolute_url(self):
        """
        Returns the url to access the doctors view.
        """

        return reverse('view_workup', args=[str(self.id)])
from django.db import models
# from doctors.models import Doctor
# from ..doctors.models import Doctor
from django.urls import reverse
# Create your models here.

class WorkUp(models.Model):

    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, default=None, blank=True, null=True)
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, default=None, blank=True, null=True)
    workup_name = models.TextField(max_length=100)
    workup_instruction = models.TextField(max_length=5000)

    def __str__(self):
        return '{0}'.format(self.workup_name)

    def get_absolute_url(self):
        """
        Returns the url to access the doctors view.
        """

        return reverse('view_workup', args=[str(self.id)])
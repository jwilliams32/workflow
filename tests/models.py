from django.db import models
# from doctors.models import Doctor
# from ..doctors.models import Doctor
from django.urls import reverse
# Create your models here.

class Test(models.Model):

    doctor = models.ManyToManyField('doctors.Doctor', related_name='tests', blank=True)
    # test_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    test_name = models.TextField(max_length=500)
    test_description = models.TextField(max_length=500)

    def __str__(self):
        return '{0}'.format(self.test_name)

    def get_absolute_url(self):
        """
        Returns the url to access the doctors view.
        """

        return reverse('view_test', args=[str(self.id)])
from django.test import TestCase

from django.test import TestCase

from workflow.doctors.models import Doctor
# from workflow.workups.models import

class DoctorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Doctor.objects.create(doctors_name='Big Larry')

    def test_doctors_name_label(self):
        doctor = Doctor.objects.get(id=1)
        field_label = doctor._meta.get_field('doctors_name').verbose_name
        self.assertEquals(field_label, 'doctors name')

    def test_doctors_name_max_length(self):
        doctor = Doctor.objects.get(id=1)
        max_length = doctor._meta.get_field('doctors__name').max_length
        self.assertEquals(max_length, 500)

    def test_clinic_type_max_length(self):
        doctor = Doctor.objects.get(id=1)
        max_length = doctor._meta.get_field('clinic_type').max_length
        self.assertEquals(max_length, 75)

    def test_description_max_length(self):
        doctor = Doctor.objects.get(id=1)
        max_length = doctor._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_bio_max_length(self):
        doctor = Doctor.objects.get(id=1)
        max_length = doctor._meta.get_field('bio').max_length
        self.assertEquals(max_length, 500)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     author = Author.objects.get(id=1)
    #     expected_object_name = f'{author.last_name}, {author.first_name}'
    #     self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        doctor = Doctor.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(doctor.get_absolute_url(), '/doctor/1')
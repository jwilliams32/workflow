from django.urls import reverse, resolve
from django.test import RequestFactory
from django.contrib.auth.models import User
from ..doctors.views import create_doctor
from mixer.backend.django import mixer
import pytest




@pytest.mark.django_db
class TestViews:

    def test_create_doctor_auth(self):
        path = reverse('create')
        request = RequestFactory().get(path)
        request.user = mixer.blend('User')

        response = create_doctor(request)
        assert response.status_code == 200

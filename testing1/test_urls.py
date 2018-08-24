from django.urls import reverse, resolve

class TestUrls:

    def test_detail_url(self):
        path = reverse('view_doctor', kwargs={'pk': 1})
        assert resolve(path).view_name == 'view_doctor'
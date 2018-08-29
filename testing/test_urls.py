from django.urls import reverse, resolve

class TestUrls:

    def test_doctor_view_url(self):
        path = reverse('view_doctor', kwargs={'pk': 1})
        assert resolve(path).view_name == 'view_doctor'

    def test_doctor_list_url(self):
        path = reverse('list_doctors')
        assert resolve(path).view_name == 'list_doctors'

    def test_testing_view_url(self):
        path = reverse('view_test', kwargs={'pk': 1})
        assert resolve(path).view_name == 'view_test'

    def test_testing_list_url(self):
        path = reverse('list_tests')
        assert resolve(path).view_name == 'list_tests'
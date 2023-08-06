from django.test import TestCase

from pfx.pfxcore.test import APIClient, TestAssertMixin


class ViewDecoratorTest(TestAssertMixin, TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_method_not_allowed(self):
        response = self.client.put('/api/authors')
        self.assertRC(response, 405)

    def test_method_not_allowed_if_non_http_method(self):
        response = self.client.generic('ILLEGAL', '/api/authors')
        self.assertEqual(response.status_code, 405)

    def test_method_not_allowed_if_not_exists(self):
        response = self.client.get('/api/does-not-exists')
        self.assertRC(response, 405)

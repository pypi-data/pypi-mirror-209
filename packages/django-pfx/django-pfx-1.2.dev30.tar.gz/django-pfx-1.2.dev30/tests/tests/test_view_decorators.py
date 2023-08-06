from django.test import TestCase

from pfx.pfxcore.test import APIClient, TestAssertMixin
from tests.views import IllegalPriorityRestView


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

    def test_explicit_priority(self):
        response = self.client.get(
            '/api/authors/priority/dynamic')
        self.assertRC(response, 200)
        self.assertJE(response, 'value', 'param')

        # With default priority, overridden.
        response = self.client.get(
            '/api/authors/priority/default')
        self.assertRC(response, 200)
        self.assertJE(response, 'value', 'param')

        response = self.client.get(
            '/api/authors/priority/priority-less')
        self.assertRC(response, 200)
        self.assertJE(response, 'value', 'param')

        response = self.client.get(
            '/api/authors/priority/priority-more')
        self.assertRC(response, 200)
        self.assertJE(response, 'value', 'more')

    def test_illegal_priority(self):
        with self.assertRaises(Exception):
            IllegalPriorityRestView.as_urlpatterns()

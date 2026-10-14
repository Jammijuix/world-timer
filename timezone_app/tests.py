from django.test import TestCase, Client
from django.urls import reverse
from .utils import get_info

class TimezoneAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timezone_app/index.html')

    def test_index_post_valid(self):
        response = self.client.post(reverse('index'), {
            'name': 'John',
            'country': 'Nigeria',
            'city': 'Lagos'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context)
        self.assertEqual(response.context['result']['country'], 'Nigeria')

    def test_index_post_invalid_country(self):
        response = self.client.post(reverse('index'), {
            'name': 'John',
            'country': 'InvalidCountryXYZ123',
            'city': 'Lagos'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context)
        self.assertIn('error', response.context['result'])

    def test_get_info_utility(self):
        result = get_info('Alice', 'United States', 'New York')
        self.assertEqual(result['name'], 'Alice')
        self.assertEqual(result['country'], 'United States')
        self.assertEqual(result['timezone'], 'America/New_York')

from django.test import TestCase
from django.urls import reverse
import json
from .views import get_random_array

class RandomArrayAPITest(TestCase):
    def test_random_array_generation(self):
        # Test the API with a sample sentence
        sentence = "This is a test sentence."
        data = {"sentence": sentence}
        response = self.client.post(reverse('get_random_array'), data)
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue('random_array' in response_data)
        self.assertEqual(len(response_data['random_array']), 500)
        
        # Ensure that all elements in the array are floats
        self.assertTrue(all(isinstance(x, float) for x in response_data['random_array']))

    def test_invalid_input(self):
        # Test the API with invalid input
        invalid_sentence = 12345
        data = {'sentence': invalid_sentence}
        response = self.client.post(reverse('get_random_array'), data)
        
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertTrue('error' in response_data)

    def test_missing_input(self):
        # Test the API with missing input
        response = self.client.post(reverse('get_random_array'))
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertTrue('error' in response_data)
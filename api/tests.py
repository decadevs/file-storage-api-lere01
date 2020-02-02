from django.test import TestCase

# Create your tests here.
from .models import Bucket
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from django.urls import reverse

class TestModel(TestCase):

    """This class defines the test suite for the model."""

    def setUp(self):

        """Define the test client and other test variables."""

        self.bkt_name = "my_bucket"
        # self.bkt_create = timezone.now()
        self.bucket = Bucket(name = self.bkt_name)

    def test_bucket_creation(self):

        """Test that a bucket is properly created from the model"""

        initial_count = Bucket.objects.count()
        self.bucket.save()
        current_count = Bucket.objects.count()
        self.assertNotEqual(initial_count, current_count)

# Define this after the ModelTestCase
class TestView(TestCase):

    """Test suite for the api views."""

    def setUp(self):

        """Define the test client and other test variables."""

        self.client = APIClient()
        self.bkt_data = {'name': 'Go to Ibiza'}

        self.response = self.client.post(
            reverse('create'),
            self.bkt_data,
            format = "json"
            )

    def test_successful_bucket_creation(self):

        """Test the api has bucket creation capability."""

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
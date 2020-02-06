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

        self.bkt_name = "my_bucket"
        # self.bkt_create = timezone.now()
        self.bucket = Bucket(name=self.bkt_name)

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

        client = APIClient()
        self.client = client
        data = {'name': 'Abdulfatai Okeremeta'}
        self.data = data
        url = reverse('create')

        response = client.post(url, data, format="json")
        self.response = response

    
    def test_successful_bucket_creation(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    
    def test_get_bucket(self):
        bkt = Bucket.objects.get()
        url = reverse('detail', kwargs = {'bucket_id': bkt.id})
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bkt)

    
    def test_update_bucket(self):
        bkt = Bucket.objects.get()
        bkt_update = {'name': 'Kolapo Ishola'}
        response = self.client.put(
            reverse('detail', kwargs={'bucket_id': bkt.id}),
            bkt_update, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_api_can_delete_bucketlist(self):
        bkt = Bucket.objects.get()
        response = self.client.delete(
            reverse('detail', kwargs={'bucket_id': bkt.id}),
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .serializers import DomainsSerializer
from .views import getDomain
from .views import getScantype
from django.conf import settings
import boto3
import os


# tests for views

class GetAllDomainsTest(APITestCase):
    client = APIClient()

    def test_get_all_domains(self):
        """
        This test ensures that all domains
        exist when we make a GET request to the domains/ endpoint.
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("domains-list")
        )
        # fetch the data
        expected = getDomain()

        serialized = DomainsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllScansTest(APITestCase):
    client = APIClient()

    def test_get_all_scans(self):
        """
        This test ensures that all domains
        exist when we make a GET request to the domains/ endpoint.
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("scans-list")
        )
        # fetch the data
        expected = getScantype()

        serialized = DomainsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

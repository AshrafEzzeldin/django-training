from django.test import TestCase
from .models import *
from django.test import Client
from artists.models import *


class AlbumTestCase(TestCase):
    def setUp(self):
        Artist.objects.create(stageName="lion", socialLink="roar")
        Artist.objects.create(stageName="tiger", socialLink="meaw")

    def test_post_album(self):
        c = Client()
        response = c.post('/albums/', {
            "releaseDate": "2015-01-28T03:00:00Z",
            "cost": "10.000",
            "artists": 1
        })
        self.assertEqual(response.status_code, 201)

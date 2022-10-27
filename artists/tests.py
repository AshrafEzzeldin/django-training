from django.test import TestCase
from .models import *
from django.test import Client
from .serializer import ArtistSerializer


class ArtistTestCase(TestCase):
    def setUp(self):
        Artist.objects.create(stageName="lion", socialLink="roar")
        Artist.objects.create(stageName="tiger", socialLink="meaw")

    # {
    #     "stageName": "lion", "socialLink": "http://127.0.0.1:8000/artists/"
    # }
    def test_get_artists(self):
        c = Client()
        response = c.get('/artists/')
        self.assertEqual(response.status_code, 200)

    def test_post_artist(self):
        c = Client()
        response = c.post('/artists/', {"stageName": "cat", "socialLink": "http://127.0.0.1:8000/albums/"})
        print(response)
        self.assertEqual(response.status_code, 201)

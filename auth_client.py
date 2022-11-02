import pytest

from albums.models import Album
from artists.models import Artist
from users.models import User
from rest_framework.test import APIClient


@pytest.fixture
def user():
    user = User(username="Ashraf",
                email="ashraf@gmail.com"
                )
    user.set_password("111111111")
    user.save()

    return user


@pytest.fixture
def auth_user(user):
    client = APIClient()
    client.force_authenticate(user)
    return client


@pytest.fixture
def notauth_user():
    return APIClient()


@pytest.fixture
def artist(auth_user):
    artist = Artist(
        stageName="Mo",
        socialLink="https://github.com/AshrafEzzeldin/django-training/tree/BLD-4%2C5-Image",
        owner_id=1
    )
    artist.save()

    return artist


@pytest.fixture
def album(artist):
    album = Album(
        name="kol",
        cost=10.1,
        releaseDate="1999-01-01",
        artists=artist,
        approved=True
    )
    album.save()
    return album

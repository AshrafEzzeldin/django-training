import pytest
from auth_client import *


@pytest.mark.django_db
def test_list(notauth_user, album):
    response = notauth_user.get("/albums/")
    assert response.data['results'][0]['name'] == 'kol'
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_suc(auth_user, artist):
    d = dict(
        name="kol",
        cost=10.1,
        releaseDate="1999-01-01"
    )
    response = auth_user.post("/albums/", d)
    assert response.status_code == 201


@pytest.mark.django_db
def test_post_fail(auth_user):
    d = dict(
        name="kol",
        cost=10.1
    )
    response = auth_user.post("/albums/", d)
    assert response.status_code == 401


@pytest.mark.django_db
def test_post_fail(notauth_user):
    d = dict(
        name="kol",
        cost=10.1
    )
    response = notauth_user.post("/albums/", d)
    assert response.status_code == 401

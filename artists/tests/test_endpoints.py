import pytest
from auth_client import *


@pytest.mark.django_db
def test_list(notauth_user, artist):
    response = notauth_user.get("/artists/")
    assert response.data['results'][0]['stageName'] == artist.stageName
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_suc(auth_user):
    d = dict(
        stageName="Mo",
        socialLink="https://github.com/AshrafEzzeldin/django-training/tree/BLD-4%2C5-Image",
        owner_id=1
    )
    response = auth_user.post("/artists/", d)
    assert response.status_code == 201


@pytest.mark.django_db
def test_post_fail(notauth_user):
    d = dict(
        stageName="Mo",
        socialLink="https://github.com/AshrafEzzeldin/django-training/tree/BLD-4%2C5-Image",
        owner_id=1
    )
    response = notauth_user.post("/artists/", d)
    assert response.status_code == 401



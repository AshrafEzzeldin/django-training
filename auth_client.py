import pytest

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

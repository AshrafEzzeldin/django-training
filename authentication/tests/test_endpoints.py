import pytest
from rest_framework.test import APIClient
from auth_client import notauth_user, auth_user, user
from users.models import User


@pytest.mark.django_db
def test_register_suc(notauth_user):
    d = dict(
        username="Ashraf",
        email="ashraf@gmail.com",
        password1="111111111",
        password2="111111111"
    )
    response = notauth_user.post("/authentication/register/", d)
    assert response.data['username'] == "Ashraf"
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_fail(notauth_user):
    d = dict(
        username="Ashraf",
        email="ashraf@gmail.com",
    )

    response = notauth_user.post("/authentication/register/", d)
    assert response.status_code == 400


@pytest.mark.django_db
def test_login_suc(user, notauth_user):
    response = notauth_user.post("/authentication/login/", dict(username="Ashraf", password="111111111"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_fail(user, notauth_user):
    response = notauth_user.post("/authentication/login/", dict(username="fail", password="111111111"))
    assert response.status_code == 400

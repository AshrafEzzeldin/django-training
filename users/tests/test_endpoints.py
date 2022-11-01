from auth_client import *


@pytest.mark.django_db
def test_get(auth_user):
    response = auth_user.get("http://localhost:8000/users/1")
    assert response.data['pk'] == 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_put_suc(auth_user):
    d = dict(
        username="Yossef",
        email='yossef@gmail.com',
        bio='my bio'
    )
    response = auth_user.put("http://localhost:8000/users/1", d)
    assert response.data['username'] == d["username"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_put_fail(auth_user):
    d = dict(
        email='yossef@gmail.com',
        bio='my bio'
    )
    response = auth_user.put("http://localhost:8000/users/1", d)
    assert response.status_code == 400


@pytest.mark.django_db
def test_put_fail_notauth(notauth_user):
    d = dict(
        username="Yossef",
        email='yossef@gmail.com',
        bio='my bio'
    )
    response = notauth_user.put("http://localhost:8000/users/1", d)
    assert response.status_code == 401


@pytest.mark.django_db
def test_patch_suc(auth_user):
    d = dict(
        email='yossef@gmail.com',
        bio='my bio'
    )
    response = auth_user.patch("http://localhost:8000/users/1", d)
    assert response.data['email'] == d["email"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_patch_fail_notauth(notauth_user):
    d = dict(
        username="Yossef",
        email='yossef@gmail.com',
        bio='my bio'
    )
    response = notauth_user.patch("http://localhost:8000/users/1", d)
    assert response.status_code == 401

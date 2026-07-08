import uuid

from tests.helpers import login


def unique_username():
    return f"pytest_{uuid.uuid4().hex[:8]}"


def test_register(client):
    response = client.post(
        "/register",
        json={
            "username": unique_username(),
            "password": "password123"
        }
    )

    assert response.status_code == 201

    body = response.get_json()

    assert body["success"] is True


def test_register_duplicate_username(client):
    username = unique_username()

    client.post(
        "/register",
        json={
            "username": username,
            "password": "password123"
        }
    )

    response = client.post(
        "/register",
        json={
            "username": username,
            "password": "password123"
        }
    )

    assert response.status_code == 400


def test_register_without_username(client):
    response = client.post(
        "/register",
        json={
            "password": "password123"
        }
    )

    assert response.status_code == 400


def test_register_without_password(client):
    response = client.post(
        "/register",
        json={
            "username": unique_username()
        }
    )

    assert response.status_code == 400


def test_login(client):
    token = login(client)

    assert token is not None


def test_login_invalid_password(client):
    response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401


def test_login_unknown_user(client):
    response = client.post(
        "/login",
        json={
            "username": "unknown",
            "password": "password"
        }
    )

    assert response.status_code == 401


def test_login_without_username(client):
    response = client.post(
        "/login",
        json={
            "password": "password123"
        }
    )

    assert response.status_code == 400


def test_login_without_password(client):
    response = client.post(
        "/login",
        json={
            "username": "admin"
        }
    )

    assert response.status_code == 400


def test_refresh_token(client):
    login_response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "admin123"
        }
    )

    assert login_response.status_code == 200

    refresh = login_response.get_json()["data"]["refresh_token"]

    response = client.post(
        "/refresh",
        json={
            "refresh_token": refresh
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True


def test_refresh_invalid_token(client):
    response = client.post(
        "/refresh",
        json={
            "refresh_token": "invalid"
        }
    )

    assert response.status_code == 401


def test_refresh_without_token(client):
    response = client.post(
        "/refresh",
        json={}
    )

    assert response.status_code == 400
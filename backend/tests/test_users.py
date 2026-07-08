from tests.helpers import login


def test_get_users(client):

    token = login(client)

    response = client.get(
        "/users",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True
    assert "data" in body

from tests.helpers import login


def test_get_user(client):

    token = login(client)

    response = client.get(
        "/users/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True  

from tests.helpers import login


def test_get_missing_user(client):

    token = login(client)

    response = client.get(
        "/users/999999",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404      

from tests.helpers import login


def test_get_me(client):

    token = login(client)

    response = client.get(
        "/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True
    assert body["data"]["username"] == "admin"    

from tests.helpers import login


def test_update_user_role(client):

    token = login(client)

    response = client.patch(
        "/users/2/role",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "role": "user"
        }
    )

    assert response.status_code == 200    

from tests.helpers import login


def test_update_invalid_role(client):

    token = login(client)

    response = client.patch(
        "/users/2/role",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "role": "manager"
        }
    )

    assert response.status_code == 400    

from tests.helpers import login


def test_delete_user(client):

    client.post(
        "/register",
        json={
            "username": "delete_me",
            "password": "password123"
        }
    )

    token = login(client)

    response = client.delete(
        "/users/2",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200    

def test_users_without_token(client):

    response = client.get("/users")

    assert response.status_code == 401    

def test_users_invalid_token(client):

    response = client.get(
        "/users",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    )

    assert response.status_code == 401   


def test_non_admin_cannot_get_users(client):

    client.post(
        "/register",
        json={
            "username": "normaluser",
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "username": "normaluser",
            "password": "password123"
        }
    )

    token = response.get_json()["data"]["access_token"]

    response = client.get(
        "/users",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 403    
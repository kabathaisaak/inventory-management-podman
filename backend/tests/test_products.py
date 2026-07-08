
from tests.helpers import login



def create_test_product(client, token):
    response = client.post(
        "/products",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Pytest Product",
            "price": 55000
        }
    )

    assert response.status_code == 201

    body = response.get_json()

    print("CREATE RESPONSE:", body)

    assert body["success"] is True

    return body["data"]["id"]


def test_create_product(client):
    token = login(client)

    response = client.post(
        "/products",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Pytest Laptop",
            "price": 55000
        }
    )

    assert response.status_code == 201

    body = response.get_json()

    print("CREATE RESPONSE:", body)

    assert body["success"] is True

    # Don't check body["data"]["name"] yet.
    # We first want to see what the API actually returns.

def test_get_product(client):
    token = login(client)

    product_id = create_test_product(client, token)

    response = client.get(
        f"/products/{product_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True
    assert body["data"]["id"] == product_id


def test_get_missing_product(client):
    token = login(client)

    response = client.get(
        "/products/999999",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404


def test_create_product_without_name(client):
    token = login(client)

    response = client.post(
        "/products",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "price": 5000
        }
    )

    assert response.status_code == 400


def test_create_product_negative_price(client):
    token = login(client)

    response = client.post(
        "/products",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Keyboard",
            "price": -20
        }
    )

    assert response.status_code == 400


def test_update_product(client):
    token = login(client)

    product_id = create_test_product(client, token)

    response = client.put(
        f"/products/{product_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Updated Laptop",
            "price": 75000
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True


def test_delete_product(client):
    token = login(client)

    product_id = create_test_product(client, token)

    response = client.delete(
        f"/products/{product_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True


def test_products_without_token(client):
    response = client.get("/products")

    assert response.status_code == 401


def test_invalid_token(client):
    response = client.get(
        "/products",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    )

    assert response.status_code == 401
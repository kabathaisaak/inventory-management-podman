from tests.helpers import login


def test_get_products(client):
    token = login(client)

    response = client.get(
        "/products",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True
    assert "data" in body


def test_get_product(client):
    token = login(client)

    response = client.get(
        "/products/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True


def test_get_missing_product(client):
    token = login(client)

    response = client.get(
        "/products/999999",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404


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

    assert body["success"] is True


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

    response = client.put(
        "/products/1",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Updated Laptop",
            "price": 75000
        }
    )

    assert response.status_code == 200


def test_delete_product(client):
    token = login(client)

    response = client.delete(
        "/products/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200


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
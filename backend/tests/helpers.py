def login(client, username="admin", password="admin123"):

    response = client.post(
        "/login",
        json={
            "username": username,
            "password": password
        }
    )

    assert response.status_code == 200

    return response.get_json()["data"]["access_token"]
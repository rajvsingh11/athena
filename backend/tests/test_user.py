from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_and_retrieve_user():
    email = f"test-{uuid4().hex}@example.com"

    create_response = client.post(
        "/api/v1/users",
        json={
            "name": "Athena Test User",
            "email": email,
        },
    )

    assert create_response.status_code == 201

    created_user = create_response.json()

    assert created_user["name"] == "Athena Test User"
    assert created_user["email"] == email
    assert isinstance(created_user["id"], int)

    user_id = created_user["id"]

    get_response = client.get(
        f"/api/v1/users/{user_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["id"] == user_id


def test_retrieve_nonexistent_user():
    response = client.get("/api/v1/users/2147483647")

    assert response.status_code == 404
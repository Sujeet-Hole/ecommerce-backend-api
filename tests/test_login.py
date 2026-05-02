from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_login():
    email = "test123@test.com"

    client.post(
        "/api/v1/registration",
        json={
            "username": "sujeet",
            "password": "123456",
            "email": email
        }
    )

    response = client.post(
        "/api/v1/login",
        json={
            "email": email,
            "password": "123456"
        }
    )

    print(response.json())

    assert response.status_code == 200
    assert "access_token" in response.json()
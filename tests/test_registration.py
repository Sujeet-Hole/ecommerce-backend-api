from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_registration():
    import uuid

    email = f"{uuid.uuid4()}@test.com"

    response = client.post(
        "/api/v1/registration",
        json={
            "username": "sujeet",
            "password": "123456",
            "email": email
        }
    )

    print(response.json())

    assert response.status_code == 200
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)


def test_login_user_not_found():
    response = client.post(
        "/api/v1/login",
        json={
            "email": "nouser@test.com",
            "password": "123456"
        }
    )

    assert response.status_code == 400
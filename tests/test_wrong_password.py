from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


def test_wrong_password():

    email = "wrongpass@test.com"

    client.post(
        "/api/v1/registration",
        json={
            "username": "user",
            "email": email,
            "password": "123456"            
        }
    )


    response = client.post(
        "/api/v1/login",
        json={
            "email" : email,
            "password" : "boom@12"
        }
    )


    assert response.status_code == 401
from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_duplicate_email():
    email = "dup@test.com"

    client.post(
        "api/v1/registration",
        json={
            "username": "user1",
            "email": email,
            "password": "123456"
        }
    )


    response = client.post(
        "api/v1/registration",
        json={
            "username" :"user2" ,
            "email" : email,
            "password" : "123456"
        }
    )

    assert response.status_code == 401



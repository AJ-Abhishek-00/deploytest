from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_full_auth_flow():

    # register
    client.post(
        "/auth/register",
        json={
            "email": "integration@example.com",
            "password": "123456"
        }
    )

    # login
    login_response = client.post(
        "/auth/login",
        json={
            "email": "integration@example.com",
            "password": "123456"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    # access protected route
    me_response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert me_response.status_code == 200

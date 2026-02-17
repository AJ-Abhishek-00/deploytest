from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "email": "unit@example.com",
            "password": "123456"
        }
    )

    assert response.status_code in [200, 400]


def test_login_user():
    response = client.post(
        "/auth/login",
        json={
            "email": "unit@example.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "email": "unit@example.com",
            "password": "123456"
        }
    )

    assert response.status_code in [200, 400]


def test_login_user():
    response = client.post(
        "/auth/login",
        json={
            "email": "unit@example.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()

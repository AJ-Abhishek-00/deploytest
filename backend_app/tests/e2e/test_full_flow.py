from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_end_to_end_flow():

    # register
    client.post(
        "/auth/register",
        json={
            "email": "e2e@example.com",
            "password": "123456"
        }
    )

    # login
    login = client.post(
        "/auth/login",
        json={
            "email": "e2e@example.com",
            "password": "123456"
        }
    )

    token = login.json()["access_token"]

    # create product
    client.post(
        "/products",
        json={
            "name": "Test Product",
            "category": "Test",
            "price": 100,
            "rating": 4.5
        }
    )

    # dashboard
    dashboard = client.get(
        "/dashboard/summary"
    )

    assert dashboard.status_code == 200

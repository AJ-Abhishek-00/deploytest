from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_products():

    response = client.get("/products")

    assert response.status_code == 200

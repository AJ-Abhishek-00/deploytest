from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_product_filter():

    response = client.get(
        "/products?category=Electronics"
    )

    assert response.status_code == 200

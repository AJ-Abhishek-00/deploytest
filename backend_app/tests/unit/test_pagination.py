from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_cursor_pagination():

    response = client.get("/products?limit=2")

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert "next_cursor" in data
    assert "has_more" in data

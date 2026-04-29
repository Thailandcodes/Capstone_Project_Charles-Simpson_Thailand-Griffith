from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200


def test_add_data():
    response = client.post(
        "/data",
        params={"country": "TestLand", "year": 2022, "temperature": 1.2}
    )
    assert response.status_code == 200


def test_filter_data():
    response = client.get("/data?country=TestLand")
    assert response.status_code == 200

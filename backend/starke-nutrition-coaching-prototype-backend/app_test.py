import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_recipe(client):
    response = client.get("/get_recipe?kcal=500&proteins=50&carbs=50&fats=10")
    assert response.status_code == 200


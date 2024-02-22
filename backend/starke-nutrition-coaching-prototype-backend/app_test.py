import pytest
from app import app
import json


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize("kcal,proteins,carbs,fats", [
    (False, 0, 0, 0),
    (1, 0, 0, 0),
    (500, 50, 50, 10),
    (800, 70, 60, 20),
])
def test_get_recipe(client, kcal, proteins, carbs, fats):
    response = client.get(f"/get_recipe?kcal={kcal}&proteins={proteins}&carbs={carbs}&fats={fats}")

    if not kcal:
        assert response.status_code == 500

    elif kcal == 1:
        assert response.content_type == "text/html; charset=utf-8"
        assert response.status_code == 200

    else:

        assert response.status_code == 200

        assert response.content_type == "application/json"

        data = json.loads(response.data)

        assert "calories" in data
        assert "carbs" in data
        assert "fat" in data
        assert "id" in data
        assert "image" in data
        assert "protein" in data
        assert "title" in data


def test_get_recipe_no_params(client):
    response = client.get("/get_recipe")

    assert response.status_code == 200
    assert response.content_type == "application/json"

    data = json.loads(response.data)

    assert "calories" in data
    assert "carbs" in data
    assert "fat" in data
    assert "id" in data
    assert "image" in data
    assert "protein" in data
    assert "title" in data

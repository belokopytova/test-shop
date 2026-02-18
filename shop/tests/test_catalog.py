import pytest
from rest_framework import status

@pytest.mark.django_db
def test_get_categories(api_client, category):
    response = api_client.get("/api/catalog/categories/")
    assert response.status_code == 200

    categories = response.data.get("results", response.data)
    assert len(categories) >= 1
    assert any(c["name"] == "Fruits" for c in categories)

@pytest.mark.django_db
def test_get_subcategories(api_client, subcategory):
    response = api_client.get("/api/catalog/categories/")
    assert response.status_code == 200

    categories = response.data.get("results", response.data)

    fruits = next(c for c in categories if c["name"] == "Fruits")
    subcats = fruits.get("subcategories", [])
    assert any(sc["name"] == "Bananas" for sc in subcats)
import pytest
from rest_framework import status

@pytest.mark.django_db
def test_cart_post_add(api_client, token, product):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    data = {"product": product.id, "quantity": 3}
    response = api_client.post("/api/cart/", data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["product"] == product.id
    assert response.data["quantity"] == 3
    assert "user" in response.data



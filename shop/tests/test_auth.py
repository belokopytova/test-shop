import pytest
from rest_framework import status

@pytest.mark.django_db
def test_login_success(api_client, user):
    data = {"username": "anna", "password": "123456"}
    response = api_client.post("/api/auth/login/", data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data
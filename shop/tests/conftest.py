import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from catalog.models import Category, SubCategory, Product

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username="anna", password="123456")

@pytest.fixture
def token(api_client, user):
    response = api_client.post("/api/auth/login/", {"username": "anna", "password": "123456"}, format="json")
    return response.data["access"]

@pytest.fixture
def category():
    return Category.objects.create(name="Fruits", slug="fruits", image="category/fruits.jpg")

@pytest.fixture
def subcategory(category):
    return SubCategory.objects.create(name="Bananas", slug="bananas", category=category, image="subcategory/bananas.jpg")

@pytest.fixture
def product(subcategory):
    return Product.objects.create(
        name="Banana",
        slug="banana",
        price=100,
        subcategory=subcategory,
        image_small="product/small/banana.jpg",
        image_medium="product/medium/banana.jpg",
        image_large="product/large/banana.jpg"
    )
from rest_framework import serializers
from .models import Category, SubCategory, Product

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="subcategory.category.name", read_only=True)
    subcategory = serializers.CharField(source="subcategory.name", read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "slug", "price", "category", "subcategory", "images")

    def get_images(self, obj):
        return [
            obj.image_small.url,
            obj.image_medium.url,
            obj.image_large.url,
        ]
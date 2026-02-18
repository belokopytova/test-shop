from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source="user.username")  # или id

    class Meta:
        model = CartItem
        fields = ("id", "user", "product", "quantity", "total")
    def get_total(self, obj):
        return obj.product.price * obj.quantity
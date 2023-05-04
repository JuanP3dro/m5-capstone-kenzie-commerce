from .models import Cart, ProductCart
from rest_framework import serializers
from products.serializers import ProductSerializer
from users.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user"]
        depth = 0

    # def create(self, validated_data):
    #     return Cart.objects.create(**validated_data)


class ProductCartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True)
    cart = CartSerializer(read_only=True)

    class Meta:
        model = ProductCart
        fields = ["id", "products", "cart", "quantity"]

    def create(self, validated_data):
        return ProductCart.objects.create(**validated_data)

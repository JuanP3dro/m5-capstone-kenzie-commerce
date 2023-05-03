from .models import Cart, ProductCart
from rest_framework import serializers
from products.serializers import ProductSerializer
from cart.serializers import CartSerializer

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id', 'products', 'user_id']

class ProductCartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    cart = CartSerializer(many=True)
    class Meta:
        model = ProductCart
        fields = ['id', 'products', 'cart', 'quantity']
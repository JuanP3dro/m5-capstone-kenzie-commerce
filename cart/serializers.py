from .models import Cart
from rest_framework import serializers
from products.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id', 'products', 'user_id']
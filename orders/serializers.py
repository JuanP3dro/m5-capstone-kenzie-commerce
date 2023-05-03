from .models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    products= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'status', 'created_at', 'user', 'products']

    def get_products(self, obj:Order):
       cart = obj.user.cart
       return cart.products
        
    def create(self, validated_data):
        return Order.objects.create(**validated_data)
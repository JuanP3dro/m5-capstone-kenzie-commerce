from .models import Order
from rest_framework import serializers
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    products= ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'status', 'created_at', 'user', 'products']

    def get_products(self, obj:Order):
       cart = obj.user.cart
       return cart.products
        
    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product in products:
            order.products.set(product)
        order.save()
        return order
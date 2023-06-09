from .models import Order, ProductOrder
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "user", "products"]
        read_only_fields = ["user"]

    def get_products(self, obj: Order):
        cart = obj.user.cart
        return cart.products

    def create(self, validated_data):
        products = validated_data.pop("products")
        order = Order.objects.create(**validated_data)
        for product in products:
            order.products.set(product)
        order.save()
        return order


class ProductReturnSerializer(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductReturnSerializer()

    class Meta:
        model = ProductOrder
        fields = ["product", "quantity"]


class OrderProductSellerSerializer(serializers.ModelSerializer):
    product = ProductReturnSerializer()
    order = OrderSerializer()

    class Meta:
        model = ProductOrder
        fields = ["product", "quantity", "order"]

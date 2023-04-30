from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'in_stock', 'is_available']
        read_only_fields = ['id', 'is_available']
        extra_kwargs = {
            'name': {'validators': [UniqueValidator(
                queryset=Product.objects.all(),message='This field must be unique.'
            )]}
        }
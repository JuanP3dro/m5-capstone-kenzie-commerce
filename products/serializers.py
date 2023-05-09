from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    # seller = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "price",
            "in_stock",
            "is_available",
            "seller",
        ]
        depth = 0
        read_only_fields = ["id", "is_available", "seller"]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Product.objects.all(),
                        message="This field must be unique.",
                    )
                ]
            }
        }

    def create(self, validated_data):
        validated_data["is_available"] = False
        if validated_data["in_stock"] > 0:
            validated_data["is_available"] = True

        return Product.objects.create(**validated_data)


class ProductReturnSerializer(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)

from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category", "price", "in_stock", "is_available"]
        read_only_fields = ["id", "is_available"]
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

        return super().create(validated_data)

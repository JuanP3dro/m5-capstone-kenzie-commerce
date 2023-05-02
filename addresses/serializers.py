from .models import Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "zip_code",
            "street",
            "number",
            "complement",
            "user_id",
        ]
        read_only_fields = ["id", "user_id"]

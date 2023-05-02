from .models import User, Address
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class AddressSerializer (serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'zip_code', 'street', 'number', 'complement', 'user_id']
        read_only_fields = ['id', 'user_id']

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'in_seller', 'is_superuser']
        read_only_fields = ['id', 'is_seller', 'is_superuser']
        extra_kwargs = {
            'username': {'validators': [UniqueValidator(
                queryset=User.objects.all(),message='This field must be unique.'
            )]},
            'email': {'validators': [UniqueValidator(
                queryset=User.objects.all(),message='This field must be unique.'
            )]},
            'password': {'write_only': True}
        }


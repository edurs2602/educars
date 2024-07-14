from rest_framework import serializers
from src.user.models import CustomUser, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['zipcode', 'district', 'city', 'street', 'uf', 'complement']


class CustomUserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'zipcode', 'address', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            cep=validated_data['zipcode'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )

        user.refresh_from_db()
        return user

from rest_framework import serializers
from src.user.models import CustomUser, Address
from src.post.models import Post, PostImage
from src.vehicle.models import Vehicle, Item


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


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']


class PostSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(many=True, read_only=True)
    image_uploads = serializers.ListField(
        child=serializers.ImageField(write_only=True),
        write_only=True,
        max_length=6
    )
    user_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user_email', 'vehicle_id', 'about', 'location', 'description', 'price', 'post_images', 'image_uploads']

    def create(self, validated_data):
        user_email = validated_data.pop('user_email')
        user = CustomUser.objects.get(email=user_email)
        image_uploads = validated_data.pop('image_uploads')
        post = Post.objects.create(user=user, **validated_data)
        for image in image_uploads:
            PostImage.objects.create(post=post, image=image)
        return post


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item']


class VehicleSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Vehicle
        fields = [
            'id', 'car_name', 'car_model', 'brand', 'color', 'year',
            'fuel_type', 'transmission', 'protected', 'car_body', 'km', 'items'
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        vehicle = Vehicle.objects.create(**validated_data)
        for item_data in items_data:
            item, created = Item.objects.get_or_create(**item_data)
            vehicle.items.add(item)
        return vehicle

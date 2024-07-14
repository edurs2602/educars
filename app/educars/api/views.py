from rest_framework import generics, viewsets
from src.user.models import CustomUser
from api.serializers import CustomUserSerializer, PostSerializer, ItemSerializer, VehicleSerializer
from src.post.models import Post
from src.vehicle.models import Vehicle, Item


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

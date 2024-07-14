from rest_framework import generics
from src.user.models import CustomUser
from api.serializers import CustomUserSerializer


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

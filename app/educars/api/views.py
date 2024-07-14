from rest_framework import generics, viewsets
from src.user.models import CustomUser
from api.serializers import CustomUserSerializer, PostSerializer
from src.post.models import Post


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

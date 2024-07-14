from django.urls import path
from api.views import CustomUserCreateView, PostViewSet

urlpatterns = [
    path('users/', CustomUserCreateView.as_view(), name='user-create'),
    path('posts/', PostViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='post-list-create'),
    path('posts/<uuid:pk>/', PostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='post-detail'),
]

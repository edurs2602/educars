from django.urls import path, include
from api.views import CustomUserCreateView, PostViewSet, VehicleViewSet, ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('users/', CustomUserCreateView.as_view(), name='user-create'),
    path('', include(router.urls))
]

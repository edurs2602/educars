from django.urls import path
from api.views import CustomUserCreateView

urlpatterns = [
    path('users/', CustomUserCreateView.as_view(), name='user-create'),
]

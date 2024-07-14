import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from src.user.models import CustomUser, Address

@pytest.mark.django_db
def test_create_user_via_api():
    client = APIClient()
    url = reverse('user-create')
    data = {
        'email': 'apiuser@example.com',
        'password': 'password123',
        'first_name': 'Api',
        'last_name': 'User',
        'zipcode': '37503-130'
    }

    response = client.post(url, data, format='json')

    # Verify response status and data
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data
    assert response.data['email'] == data['email']
    assert response.data['first_name'] == data['first_name']
    assert response.data['last_name'] == data['last_name']
    assert response.data['zipcode'] == data['zipcode']
    assert 'address' in response.data

    # Verify user is created
    user = CustomUser.objects.get(email=data['email'])
    assert user is not None

    # Verify address is created
    address = Address.objects.get(user=user)
    assert address.zipcode == data['zipcode']
    assert address.city != 'N/A'
    assert address.street != 'N/A'
    assert address.district != 'N/A'
    assert address.user == user

@pytest.mark.django_db
def test_create_user_without_zipcode_via_api():
    client = APIClient()
    url = reverse('user-create')
    data = {
        'email': 'apiuser2@example.com',
        'password': 'password123',
        'first_name': 'Api',
        'last_name': 'User'
    }

    response = client.post(url, data, format='json')

    # Verify response status and data
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data
    assert response.data['email'] == data['email']
    assert response.data['first_name'] == data['first_name']
    assert response.data['last_name'] == data['last_name']
    assert response.data['zipcode'] is None
    assert 'address' not in response.data

    # Verify user is created
    user = CustomUser.objects.get(email=data['email'])
    assert user is not None

    # Verify address is not created
    assert not Address.objects.filter(user=user).exists()

import pytest
from src.user.models import CustomUser, Address

@pytest.mark.django_db
def test_create_user_with_address():
    email = 'testuser@example.com'
    password = 'password123'
    first_name = 'John'
    last_name = 'Doe'
    zipcode = '37503-130'

    user = CustomUser.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        cep=zipcode
    )

    # Verify user is created
    assert user.id is not None
    assert user.email == email
    assert user.first_name == first_name
    assert user.last_name == last_name
    assert user.zipcode == zipcode

    # Verify address is created
    address = Address.objects.get(user=user)
    assert address.zipcode == zipcode
    assert address.city != 'N/A'
    assert address.street != 'N/A'
    assert address.district != 'N/A'
    assert address.user == user

@pytest.mark.django_db
def test_create_user_without_address():
    email = 'testuser2@example.com'
    password = 'password123'
    first_name = 'Jane'
    last_name = 'Doe'

    user = CustomUser.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    # Verify user is created
    assert user.id is not None
    assert user.email == email
    assert user.first_name == first_name
    assert user.last_name == last_name
    assert user.zipcode is None

    # Verify address is not created
    assert not Address.objects.filter(user=user).exists()

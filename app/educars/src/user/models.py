import uuid
import brazilcep
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save

from ..email_user.views import send_welcome_email
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    username = models.CharField(_("username"), max_length=150, blank=True, null=True, unique=True)
    zipcode = models.CharField(_("zipcode"), max_length=10, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.id}"


@receiver(post_save, sender=CustomUser)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(
            instance.email,
            instance.first_name,
            instance.last_name,
            instance.date_joined.strftime("%Y-%m-%d")
        )


class Address(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="address")
    zipcode = models.CharField(_("zipcode"), max_length=10)
    district = models.CharField(_("bairro"), max_length=100)
    city = models.CharField(_("cidade"), max_length=100)
    uf = models.CharField(_("uf"), max_length=2)

    @classmethod
    def create_from_cep(cls, user, cep):
        address_data = brazilcep.get_address_from_cep(cep)
        return cls.objects.create(
            user=user,
            zipcode=address_data.get('cep', cep),
            district=address_data.get('district', 'N/A'),
            city=address_data.get('city', 'N/A'),
            uf=address_data.get('uf', 'N/A'),
        )

    def __str__(self):
        return f"{self.city}, {self.district} - {self.uf}"

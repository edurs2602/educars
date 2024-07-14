import uuid

from django.db import models
from ..vehicle.models import Vehicle


class Contact(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=False,
        null=False
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    phone = models.CharField(
        max_length=45
    )


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=False,
        null=False
    )

    vehicle_id = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    about = models.TextField(
        blank=False,
        null=False
    )

    location = models.TextField(
        blank=False,
        null=False
    )

    description = models.TextField(
        blank=False,
        null=False
    )

    price = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    images = models.ImageField(
        default=None
    )


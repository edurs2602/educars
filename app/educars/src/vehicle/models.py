import uuid

from django.db import models
from .options import *


class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )

    item = models.TextField()

    def __str__(self):
        return self.item


class Vehicle(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=False,
        null=False,
        editable=False
    )

    car_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default=""
    )

    car_model = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        default="",
        choices=CAR_MODELS
    )

    brand = models.CharField(
        max_length=60,
        blank=False,
        null=False,
        default="",
        choices=CAR_BRANDS
    )

    color = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )

    year = models.CharField(
        max_length=4,
        blank=False,
        null=False
    )

    fuel_type = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        choices=FUEL_TYPES,
        default=FUEL_TYPES[0]
    )

    transmission = models.CharField(
        max_length=40,
        blank=False,
        null=False,
        choices=TRANSMISSION_TYPES,
        default=TRANSMISSION_TYPES[0]
    )

    protected = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    km = models.CharField(
        max_length=15,
        blank=False,
        null=False
    )

    items = models.ManyToManyField(
        Item,
        related_name='vehicles'
    )

    def __str__(self):
        return f"{self.car_name} - {self.car_model} - {self.color}"


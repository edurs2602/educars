import uuid

from django.db import models


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
        null=False
    )

    car_model = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default=""
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
        max_length=25,
        blank=False,
        null=False
    )

    cambium = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    protected = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    car_body = models.CharField(
        max_length=30,
        blank=False,
        null=False
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
        return f"{self.car_model} - {self.color}"

import uuid

from django.db import models


class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
    )

    item = models.TextField()


class Vehicle(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=False,
        null=False
    )

    chassi = models.CharField(
        max_length=45,
        blank=False,
        null=False
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

    itens_id = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

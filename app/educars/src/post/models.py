import os
import uuid

from django.db import models
from ..vehicle.models import Vehicle
from ..user.models import CustomUser


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


def post_image_upload_to(instance, filename):
    return os.path.join('images', str(instance.post.id), filename)


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=False,
        null=False
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=""
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

    def __str__(self):
        return f"{self.vehicle_id} - {self.description}"


class PostImage(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=False,
        null=False
    )

    post = models.ForeignKey(
        Post,
        related_name='post_images',
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to=post_image_upload_to
    )

    def __str__(self):
        return str(self.image)

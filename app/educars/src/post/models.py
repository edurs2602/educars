import os
import shutil
import uuid
from django.db.models.signals import post_delete
from django.db import models
from ..vehicle.models import Vehicle
from ..user.models import CustomUser
from django.dispatch import receiver
from django.conf import settings


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
        null=False,
        editable=False
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

    def finalize(self):
        self.delete()


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


# Sinal para deletar imagens e a pasta quando o Post é deletado
@receiver(post_delete, sender=Post)
def delete_post_images_and_folder(sender, instance, **kwargs):
    # Caminho da pasta do post
    post_folder = os.path.join(settings.MEDIA_ROOT, 'images', str(instance.id))
    # Deletar todos os PostImage associados
    for post_image in instance.post_images.all():
        if post_image.image:
            if os.path.isfile(post_image.image.path):
                os.remove(post_image.image.path)
        post_image.delete()
    # Deletar a pasta do post
    if os.path.isdir(post_folder):
        shutil.rmtree(post_folder)

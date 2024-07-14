from django.test import TestCase
from ..vehicle.models import Vehicle
from .models import Contact, Post
import uuid


class ContactModelTest(TestCase):

    def test_create_contact(self):
        # Test creating a Contact instance
        contact_instance = Contact.objects.create(
            email="contact@example.com",
            phone="123456789"
        )
        self.assertIsInstance(contact_instance, Contact)
        self.assertEqual(contact_instance.email, "contact@example.com")
        self.assertEqual(contact_instance.phone, "123456789")

    def test_str_method(self):
        # Test the string representation of the Contact instance
        contact_instance = Contact.objects.create(
            email="contact@example.com",
            phone="123456789"
        )
        self.assertEqual(str(contact_instance), "contact@example.com")


class PostModelTest(TestCase):

    def setUp(self):
        # Create a Vehicle instance for the ForeignKey field
        self.vehicle_instance = Vehicle.objects.create(
            chassi="123456789012345678901234567890123456789012345",
            color="Blue",
            year="2023",
            fuel_type="Gasoline",
            cambium="Automatic",
            protected=True,
            car_body="Sedan",
            km="15000",
            itens_id=uuid.uuid4()
        )

    def test_create_post(self):
        # Test creating a Post instance
        post_instance = Post.objects.create(
            vehicle_id=self.vehicle_instance,
            about="About the vehicle",
            location="Location of the vehicle",
            description="Detailed description of the vehicle",
            price=10000,
            images="path/to/image.jpg"
        )
        self.assertIsInstance(post_instance, Post)
        self.assertEqual(post_instance.vehicle_id, self.vehicle_instance)
        self.assertEqual(post_instance.about, "About the vehicle")
        self.assertEqual(post_instance.location, "Location of the vehicle")
        self.assertEqual(post_instance.description, "Detailed description of the vehicle")
        self.assertEqual(post_instance.price, 10000)
        self.assertEqual(post_instance.images, "path/to/image.jpg")

    def test_default_uuid(self):
        # Test that the default UUID is generated
        post_instance = Post.objects.create(
            vehicle_id=self.vehicle_instance,
            about="About the vehicle",
            location="Location of the vehicle",
            description="Detailed description of the vehicle",
            price=15000,
            images="path/to/another_image.jpg"
        )
        self.assertIsInstance(post_instance.id, uuid.UUID)

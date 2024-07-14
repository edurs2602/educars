from django.test import TestCase
from .models import Item, Vehicle
import uuid


class ItemModelTest(TestCase):

    def test_create_item(self):
        # Test creating an Item instance
        item_instance = Item.objects.create(
            id=uuid.uuid4(),
            item="Test Item Description"
        )
        self.assertIsInstance(item_instance, Item)
        self.assertEqual(item_instance.item, "Test Item Description")

    def test_str_method(self):
        # Test the string representation of the Item instance
        item_instance = Item.objects.create(
            id=uuid.uuid4(),
            item="Test Item Description"
        )
        self.assertEqual(str(item_instance), "Test Item Description")


class VehicleModelTest(TestCase):

    def setUp(self):
        # Create an Item instance for the ForeignKey field
        self.item_instance = Item.objects.create(
            id=uuid.uuid4(),
            item="Test Item Description"
        )

    def test_create_vehicle(self):
        # Test creating a Vehicle instance
        vehicle_instance = Vehicle.objects.create(
            chassi="123456789012345678901234567890123456789012345",
            color="Blue",
            year="2023",
            fuel_type="Gasoline",
            cambium="Automatic",
            protected=True,
            car_body="Sedan",
            km="15000",
            itens_id=self.item_instance
        )
        self.assertIsInstance(vehicle_instance, Vehicle)
        self.assertEqual(vehicle_instance.chassi, "123456789012345678901234567890123456789012345")
        self.assertEqual(vehicle_instance.color, "Blue")
        self.assertEqual(vehicle_instance.year, "2023")
        self.assertEqual(vehicle_instance.fuel_type, "Gasoline")
        self.assertEqual(vehicle_instance.cambium, "Automatic")
        self.assertTrue(vehicle_instance.protected)
        self.assertEqual(vehicle_instance.car_body, "Sedan")
        self.assertEqual(vehicle_instance.km, "15000")
        self.assertEqual(vehicle_instance.itens_id, self.item_instance)

    def test_default_uuid(self):
        # Test that the default UUID is generated
        vehicle_instance = Vehicle.objects.create(
            chassi="123456789012345678901234567890123456789012345",
            color="Red",
            year="2023",
            fuel_type="Diesel",
            cambium="Manual",
            protected=False,
            car_body="SUV",
            km="20000",
            itens_id=self.item_instance
        )
        self.assertIsInstance(vehicle_instance.id, uuid.UUID)


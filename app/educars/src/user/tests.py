from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserModelTest(TestCase):

    def setUp(self):
        self.user_model = get_user_model()

    def test_create_user(self):
        # Test creating a CustomUser instance
        user = self.user_model.objects.create_user(
            email="testuser@example.com",
            password="password123"
        )
        self.assertIsInstance(user, self.user_model)
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertIsNotNone(user.date_joined)

    def test_create_superuser(self):
        # Test creating a CustomUser instance with superuser status
        admin_user = self.user_model.objects.create_superuser(
            email="adminuser@example.com",
            password="password123"
        )
        self.assertIsInstance(admin_user, self.user_model)
        self.assertEqual(admin_user.email, "adminuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertIsNotNone(admin_user.date_joined)

    def test_unique_email(self):
        # Test that email field is unique
        self.user_model.objects.create_user(
            email="unique@example.com",
            password="password123"
        )
        with self.assertRaises(Exception):
            self.user_model.objects.create_user(
                email="unique@example.com",
                password="password456"
            )

    def test_str_method(self):
        # Test the string representation of the CustomUser instance
        user = self.user_model.objects.create_user(
            email="struser@example.com",
            password="password123"
        )
        self.assertEqual(str(user), "struser@example.com")

    def test_user_manager_create_user(self):
        # Test creating a user using the custom manager
        user = self.user_model.objects.create_user(
            email="manageruser@example.com",
            password="password123"
        )
        self.assertIsInstance(user, self.user_model)
        self.assertEqual(user.email, "manageruser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertIsNotNone(user.date_joined)

    def test_user_manager_create_superuser(self):
        # Test creating a superuser using the custom manager
        admin_user = self.user_model.objects.create_superuser(
            email="managersuperuser@example.com",
            password="password123"
        )
        self.assertIsInstance(admin_user, self.user_model)
        self.assertEqual(admin_user.email, "managersuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertIsNotNone(admin_user.date_joined)

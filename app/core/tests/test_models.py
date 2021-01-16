from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """Test creating a new user with an email is successful"""
        email = "test@gmail.com"
        password = "zaqwsX1@"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@GMAil.com"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com", "test123")

        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)

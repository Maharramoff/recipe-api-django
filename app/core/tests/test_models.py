from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        email = 'test@demo.az'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@DEMO.AZ'
        user = get_user_model().objects.create_user(email, 'test123456')
        self.assertEqual(user.email, email.lower())

    def test_if_new_user_email_valide(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123456')

    def test_if_superuser_created(self):
        user = get_user_model().objects.create_superuser(
            'test@demo.az',
            'test123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

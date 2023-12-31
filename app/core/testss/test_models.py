"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    "Test cases for models"

    def test_create_user_with_email_successfully(self):
        "Test createing a user with an email is successful"
        email = "test@example.com"
        password = "test"

        user = get_user_model().objects.create_user(
            email=email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email,'sample123')
            self.assertEqual(user.email,expected)

    def test_new_user_without_email_raises_error(self):
        """ Test that creating a user without email raises the error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')    
    
    def test_creat_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com', 
            'test12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
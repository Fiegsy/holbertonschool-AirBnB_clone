#!/usr/bin/python3
"""Unit tests for the User class"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_user_creation_and_attributes(self):
        """Test user creation and attribute assignment"""
        user = User(email="jessica.jones@mail.com", first_name="Jessica", last_name="Jones", password="alias")
        self.assertEqual(user.email, "jessica.jones@mail.com")
        self.assertEqual(user.first_name, "Jessica")
        self.assertEqual(user.last_name, "Jones")
        self.assertEqual(user.password, "alias")

    def test_string_representation(self):
        """Test the __str__ method"""
        user = User(email="luke.cage@mail.com", first_name="Luke", last_name="Cage", password="bulletproof")
        expected_str = "User(email='luke.cage@mail.com', first_name='Luke', last_name='Cage')"
        self.assertEqual(str(user), expected_str)

    def test_attribute_types(self):
        """Test attribute types"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.password, str)

    def test_valid_instance_id(self):
        """Test that the user instance has a valid ID"""
        user = User(email="danny.rand@mail.com", first_name="Danny", last_name="Rand", password="ironfist")
        self.assertTrue(hasattr(user, 'id') and isinstance(user.id, str) and len(user.id) == 36)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        user = User(email="frank.castle@mail.com", first_name="Frank", last_name="Castle", password="punisher")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertTrue(all(key in user_dict.keys() for key in ['__class__', 'id', 'created_at', 'updated_at', 'email', 'first_name', 'last_name', 'password']))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unit tests for the City class"""


import unittest
from models.city import City


class TestCityAttributes(unittest.TestCase):
    """Test case for City class attributes"""

    def test_default_attributes(self):
        """Test default attribute values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_custom_attributes(self):
        """Test setting custom attribute values"""
        city = City(state_id="123", name="Test City")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "Test City")


if __name__ == '__main__':
    unittest.main()

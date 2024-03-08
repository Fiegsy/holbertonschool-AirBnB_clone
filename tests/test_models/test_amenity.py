#!/usr/bin/python3
"""Unit tests for the Amenity class"""


import unittest
from models.amenity import Amenity


class TestAmenityAttributes(unittest.TestCase):
    """Test case for Amenity class attributes"""

    def test_default_attributes(self):
        """Test default attribute values"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_custom_attributes(self):
        """Test setting custom attribute values"""
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main()

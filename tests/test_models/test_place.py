#!/usr/bin/python3
"""Unit tests for the Place class"""


import unittest
from models.place import Place


class TestPlaceAttributes(unittest.TestCase):
    """Test case for Place class attributes"""

    def test_default_attributes(self):
        """Test default attribute values"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_custom_attributes(self):
        """Test setting custom attribute values"""
        place = Place(city_id="123", user_id="456", name="Test Place", description="Test Description",
                      number_rooms=2, number_bathrooms=1, max_guest=4, price_by_night=100,
                      latitude=40.7128, longitude=-74.0060, amenity_ids=["a1", "a2"])
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "Test Description")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["a1", "a2"])


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unit tests for the Review class"""


import unittest
from models.review import Review


class TestReviewAttributes(unittest.TestCase):
    """Test case for Review class attributes"""

    def test_default_place_id(self):
        """Test default place_id attribute"""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_custom_place_id(self):
        """Test setting a custom place_id"""
        review = Review(place_id="12345")
        self.assertEqual(review.place_id, "12345")

    def test_custom_place_id_assignment(self):
        """Test assigning a custom place_id"""
        review = Review()
        review.place_id = "54321"
        self.assertEqual(review.place_id, "54321")


class TestReviewMethods(unittest.TestCase):
    """Test case for Review class methods"""

    def test_review_representation(self):
        """Test the __str__ method"""
        review = Review(place_id="12345")
        self.assertEqual(str(review), "<Review: Place ID 12345>")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        review = Review(place_id="12345")
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['place_id'], "12345")
        self.assertTrue(all(key in review_dict.keys() for key in ['__class__', 'id', 'created_at', 'updated_at', 'place_id']))


if __name__ == '__main__':
    unittest.main()

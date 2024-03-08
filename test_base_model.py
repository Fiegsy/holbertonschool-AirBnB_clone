#!/usr/bin/python3
"""Unit tests for the AirBnB clone console project."""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def test_creation(self):
        """Test the creation of a BaseModel instance."""
        my_model = BaseModel()
        self.assertIsNotNone(my_model)

    def test_attributes(self):
        """Test if BaseModel instance has expected attributes."""
        my_model = BaseModel()
        attributes = ["id", "created_at", "updated_at"]
        for attr in attributes:
            self.assertTrue(hasattr(my_model, attr))

    def test_save_updates_updated_at(self):
        """Test if save() updates the updated_at attribute."""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_returns_dictionary(self):
        """Test if to_dict() returns a dictionary."""
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertIsInstance(my_dict, dict)

    def test_from_dict_creates_instance_with_same_attributes(self):
        """Test if from_dict() creates instance with same attributes."""
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        new_model = BaseModel(**my_dict)
        self.assertEqual(my_model.__dict__, new_model.__dict__)

    def test_str_representation(self):
        """Test if __str__ method returns the expected string representation."""
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)


if __name__ == "__main__":
    unittest.main()

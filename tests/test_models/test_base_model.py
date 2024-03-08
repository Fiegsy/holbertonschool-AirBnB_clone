import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestDifferentBaseModel(unittest.TestCase):
    """Different Test cases for the BaseModel class"""

    def test_updated_at_updated_after_save(self):
        """Test if updated_at attribute is updated after calling save()"""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_contains_name(self):
        """Test if the returned dictionary from to_dict() contains the 'name' attribute"""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model_dict = my_model.to_dict()
        self.assertIn("name", my_model_dict)

    def test_str_contains_model_name(self):
        """Test if the __str__ method returns a string containing the model name"""
        my_model = BaseModel()
        my_model.name = "Test Model"
        self.assertIn("Test Model", str(my_model))

    def test_instance_attributes_are_datetime(self):
        """Test if created_at and updated_at attributes are instances of datetime"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()

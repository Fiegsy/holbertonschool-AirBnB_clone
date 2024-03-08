import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel


class DifferentTestBaseModel(unittest.TestCase):
    """
    Unique test class for BaseModel.
    """

    def test_id_is_unique(self):
        """
        Test if the IDs generated are unique.
        """
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_created_at_is_past(self):
        """
        Test if created_at is in the past.
        """
        base_model = BaseModel()
        now = datetime.now()
        self.assertLess(base_model.created_at, now)

    def test_updated_at_is_future(self):
        """
        Test if updated_at is in the future.
        """
        base_model = BaseModel()
        future_time = datetime.now() + timedelta(days=1)
        self.assertGreater(base_model.updated_at, future_time)

    def test_str_method_returns_str(self):
        """
        Test if __str__ returns a string.
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model.__str__(), str)

    def test_save_method_updates_updated_at(self):
        """
        Test if save method updates updated_at.
        """
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)

    def test_to_dict_contains_expected_keys(self):
        """
        Test if to_dict method returns dictionary with expected keys.
        """
        base_model = BaseModel()
        dict_representation = base_model.to_dict()
        self.assertIn('id', dict_representation)
        self.assertIn('created_at', dict_representation)
        self.assertIn('updated_at', dict_representation)
        self.assertIn('__class__', dict_representation)


if __name__ == "__main__":
    unittest.main()

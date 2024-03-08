import unittest
from datetime import datetime
from models.base_model import BaseModel


class DifferentTestBaseModel(unittest.TestCase):
    """Test class for a different version of BaseModel"""

    def test_custom_id_type(self):
        """Test the id attribute type"""
        base = BaseModel()
        self.assertEqual(str, type(base.id))

    def test_created_at_instance(self):
        """Test created_at attribute instance"""
        base = BaseModel()
        self.assertIsInstance(base.created_at, datetime)

        base.created_at = datetime.now()
        self.assertIsNotNone(base.created_at)

    def test_updated_at_instance(self):
        """Test updated_at attribute instance"""
        base = BaseModel()
        self.assertIsInstance(base.updated_at, datetime)

        base.created_at = datetime.now()
        self.assertIsNotNone(base.updated_at)

    def test_custom_str_type(self):
        """Test __str__ method type"""
        self.assertEqual(str, type(BaseModel.__str__(self)))

    def test_custom_save_method(self):
        """Test custom save method"""
        base = BaseModel()
        base.name = "MyModel"
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

        with open("custom_file.json", "r", encoding='utf-8') as f:
            self.assertIn(base.name, f.read())


if __name__ == '__main__':
    unittest.main()

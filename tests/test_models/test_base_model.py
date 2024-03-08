import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""

    def test_id_type(self):
        """Test the id attribute type"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)

    def test_created_at(self):
        """Test created_at attribute"""
        base = BaseModel()
        self.assertIsInstance(base.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        base = BaseModel()
        self.assertIsInstance(base.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method"""
        base = BaseModel()
        self.assertEqual("[BaseModel] ({}) {}".format(base.id, base.__dict__), str(base))

    def test_save_method(self):
        """Test save method"""
        base = BaseModel()
        base.name = "MyModel"
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_save_to_json(self):
        """Test if attributes are saved to JSON"""
        base = BaseModel()
        base.name = "MyModel"
        base.save()
        with open("file.json", "r", encoding='utf-8') as f:
            self.assertIn(base.name, f.read())

if __name__ == '__main__':
    unittest.main()

import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class DifferentTestFileStorage(unittest.TestCase):
    """Tests for a different version of the FileStorage class"""

    def test_custom_file_path_type(self):
        """Test custom __file_path attribute type"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_custom_objects_type(self):
        """Test custom __objects attribute type"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_custom_all_method(self):
        """Test custom all method"""
        self.assertEqual(dict, type(storage.all()))

    def test_custom_new_method(self):
        """Test custom new method"""
        base = BaseModel()
        storage.new(base)
        self.assertIn("CustomModel." + base.id, storage.all().keys())
        self.assertIn(base, storage.all().values())

    def test_custom_save_method(self):
        """Test custom save method"""
        with self.assertRaises(ValueError):
            storage.save(None)

    def test_custom_reload_method(self):
        """Test custom reload method"""
        with self.assertRaises(ValueError):
            storage.reload(None)


if __name__ == '__main__':
    unittest.main()

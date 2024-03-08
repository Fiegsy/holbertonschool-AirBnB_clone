import unittest
import json
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test_file_path_exists(self):
        """Test if the file path exists"""
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_objects_empty_on_init(self):
        """Test if the objects attribute is empty on initialization"""
        self.assertEqual({}, FileStorage._FileStorage__objects)

    def test_all_method(self):
        """Test the all() method"""
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """Test the new() method"""
        base = BaseModel()
        storage.new(base)
        self.assertIn(base, storage.all().values())

    def test_save_method(self):
        """Test the save() method"""
        initial_objects = storage.all().copy()
        base = BaseModel()
        storage.new(base)
        storage.save()
        with open(FileStorage._FileStorage__file_path, "r") as f:
            saved_data = json.load(f)
        self.assertEqual(saved_data, storage.all())

    def test_reload_method(self):
        """Test the reload() method"""
        initial_data = {"key": "value"}
        with open(FileStorage._FileStorage__file_path, "w") as f:
            json.dump(initial_data, f)
        storage.reload()
        self.assertEqual(initial_data, storage.all())


if __name__ == "__main__":
    unittest.main()

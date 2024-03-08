#!/usr/bin/python3
"""Unit tests for the FileStorage class"""

import unittest
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test_file_path_attribute(self):
        """Test the __file_path attribute type"""
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_objects_attribute(self):
        """Test the __objects attribute type"""
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all_method(self):
        """Test the all() method"""
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), len(FileStorage._FileStorage__objects))

    def test_new_method(self):
        """Test the new() method"""
        base = BaseModel()
        storage.new(base)
        self.assertIn(f"{base.__class__.__name__}.{base.id}", storage.all())

    def test_save_method_invalid_input(self):
        """Test the save() method with invalid input"""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method(self):
        """Test the reload() method"""
        initial_data = {"key": "value"}
        with open(FileStorage._FileStorage__file_path, "w") as f:
            json.dump(initial_data, f)
        storage.reload()
        self.assertEqual(storage.all(), initial_data)


if __name__ == "__main__":
    unittest.main()

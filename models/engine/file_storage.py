import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test_file_path_attribute_type(self):
        """Test the type of __file_path attribute"""
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_objects_attribute_type(self):
        """Test the type of __objects attribute"""
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all_method_type(self):
        """Test the type of the return value of the all method"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_method_adds_object(self):
        """Test if new method adds an object to __objects"""
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        self.assertIn(base_model.__class__.__name__ + "." + base_model.id, storage.all().keys())
        self.assertEqual(storage.all()[base_model.__class__.__name__ + "." + base_model.id], base_model)

    def test_save_method_raises_error(self):
        """Test if save method raises TypeError"""
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method_raises_error(self):
        """Test if reload method raises TypeError"""
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()

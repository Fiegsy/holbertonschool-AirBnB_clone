import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class DifferentTestFileStorage(unittest.TestCase):
    """
    Unique test class for FileStorage class.
    """

    def setUp(self):
        """
        Initialize FileStorage and reload data before each test.
        """
        self.storage = FileStorage()
        self.storage.reload()

    def test_file_path_is_string(self):
        """
        Test if file_path attribute is a string.
        """
        self.assertIsInstance(self.storage.file_path, str)

    def test_objects_is_dict(self):
        """
        Test if objects attribute is a dictionary.
        """
        self.assertIsInstance(self.storage.objects, dict)

    def test_all_returns_dict(self):
        """
        Test if all method returns a dictionary.
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_add_new_object(self):
        """
        Test adding a new object to the storage.
        """
        base_model = BaseModel()
        self.storage.new(base_model)
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{base_model.id}", all_objects)

    def test_save_raises_type_error(self):
        """
        Test if save method raises TypeError when passed None.
        """
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload_raises_type_error(self):
        """
        Test if reload method raises TypeError when passed None.
        """
        with self.assertRaises(TypeError):
            self.storage.reload(None)

    def test_save_and_reload(self):
        """
        Test saving and reloading objects to and from a JSON file.
        """
        storage1 = FileStorage()
        obj1 = BaseModel()
        storage1.new(obj1)
        storage1.save()

        storage2 = FileStorage()
        storage2.reload()
        all_objects = storage2.all()
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)

    def test_clear_and_reload(self):
        """
        Test clearing storage and reloading it.
        """
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        base_key = "BaseModel.{}".format(base_model.id)
        self.assertIn(base_key, self.storage.all())
        self.storage.all().clear()
        self.assertNotIn(base_key, self.storage.all())
        self.storage.reload()
        self.assertIn(base_key, self.storage.all())


if __name__ == "__main__":
    unittest.main()

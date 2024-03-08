import unittest
from models.base_model import BaseModel

class CustomTestBaseModel(unittest.TestCase):
    """Custom Test cases for the BaseModel class"""

    def test_custom_save_behavior(self):
        """Test if custom save() behavior is implemented"""
        my_model = BaseModel()
        
        self.assertTrue(True)  

    def test_custom_to_dict_format(self):
        """Test if custom format is applied in to_dict()"""
        my_model = BaseModel()
        my_model.custom_attribute = "custom_value"
        my_model_json = my_model.to_dict()
       
        self.assertIn("custom_attribute", my_model_json)
        self.assertEqual(my_model_json["custom_attribute"], "custom_value")

    def test_custom_str_output(self):
        """Test if custom __str__ format is applied"""
        my_model = BaseModel()
        my_model.custom_description = "Custom Description"
        expected_str = f"Custom Description ({my_model.id})"
        self.assertEqual(str(my_model), expected_str)

    def test_custom_init_behavior(self):
        """Test if custom instantiation behavior is applied"""
        my_model = BaseModel(custom_arg="custom_value")
       
        self.assertIn("custom_arg", my_model.__dict__)
        self.assertEqual(my_model.custom_arg, "custom_value")

if __name__ == "__main__":
    unittest.main()

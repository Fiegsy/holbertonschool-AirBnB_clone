import json
import os
from models.base_model import BaseModel  # Assuming BaseModel is defined in models.base_model module


class FileStorage:
    """Class for handling file storage"""

    def __init__(self, file_path='file.json'):
        """Initialize the FileStorage instance with a file path."""
        self.file_path = file_path
        self.objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return self.objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = f"{type(obj).__name__}.{obj.id}"
        self.objects[key] = obj

    def save(self):
        """Serialize objects to JSON and save to file."""
        serialized_objects = {}
        for key, obj in self.objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserialize JSON file and reload objects into storage."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                serialized_objects = json.load(f)

            for key, obj_data in serialized_objects.items():
                class_name = obj_data['__class__']
                if class_name == 'BaseModel':  # Check if the class is BaseModel
                    new_obj = BaseModel(**obj_data)
                    self.objects[key] = new_obj

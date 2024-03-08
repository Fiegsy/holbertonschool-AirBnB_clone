from uuid import uuid4
from datetime import datetime
from models import storage


class DifferentBaseModel:
    """Defines a different version of the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Constructor method for the DifferentBaseModel class.
        Initializes the instance's unique id and saves the datetime of
        creation and update.

        Args:
            *args (tuple): New object's attributes
            **kwargs (dict): New object's attributes
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for attr, value in kwargs.items():
                if attr in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if attr != "__class__":
                    setattr(self, attr, value)

    def __str__(self):
        """Overwrites the __str__ method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

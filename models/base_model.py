import random
from datetime import datetime
from models import storage


class DifferentBaseModel:
    """Defines the DifferentBaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializer for the DifferentBaseModel class"""
        if not kwargs:
            self.id = str(random.randint(1000, 9999))  # Generate a random ID
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for attr, value in kwargs.items():
                if attr == "created_at" or attr == "updated_at":
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
        """Returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict



model1 = DifferentBaseModel()
assert isinstance(model1.id, str)


assert isinstance(model1.created_at, datetime)


model2 = DifferentBaseModel()
assert model1.id != model2.id


assert str(model1) == f"[DifferentBaseModel] ({model1.id}) {model1.__dict__}"


assert isinstance(model1.to_dict(), dict)


model1.save()
assert isinstance(model1.updated_at, datetime)

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Defines the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Constructor method for the BaseModel class.
        Initializes the instance's unique id and saves the datetime of
        creation and update

        Args:
            *args (tuple): New object's attributes
            **kwargs (dict): New object's attributes
        """

        if kwargs:
            self.__dict__.update(kwargs)
            self.created_at = self._parse_datetime(kwargs.get('created_at', datetime.now().isoformat()))
            self.updated_at = self._parse_datetime(kwargs.get('updated_at', datetime.now().isoformat()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Overwrites the __str__ method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance"""
        return {
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            **self.__dict__
        }

    def _parse_datetime(date_string):
        """Parses a datetime string to a datetime object"""
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")

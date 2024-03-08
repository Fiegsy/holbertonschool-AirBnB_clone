from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """Base class for all other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Initialize an instance of BaseModel"""
        if kwargs:
            self._initialize_from_kwargs(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            storage.new(self)

    def _initialize_from_kwargs(self, kwargs):
        """Initialize instance attributes from kwargs"""
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, self._parse_value(key, value))

    def _parse_value(self, key, value):
        """Parse specific values if needed"""
        if key in ['created_at', 'updated_at']:
            return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        return value

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        attrs = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attrs})"

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        return {
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

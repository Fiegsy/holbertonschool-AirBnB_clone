from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base model class for other classes to inherit from."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

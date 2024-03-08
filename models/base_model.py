from datetime import datetime
import random
import hashlib


class UniqueBaseModel:
    """
    A unique base model class with custom attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of UniqueBaseModel with custom attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "creation_date" or key == "last_updated":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.unique_id = hashlib.sha1(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
            self.creation_date = datetime.now()
            self.last_updated = datetime.now()

    def __str__(self):
        """
        Returns a unique string representation of UniqueBaseModel instance.
        """
        return f"UniqueBaseModel: ID={self.unique_id}, Attributes={self.__dict__}"

    def save(self):
        """
        Updates the last_updated attribute with the current datetime.
        """
        self.last_updated = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all attributes of UniqueBaseModel instance.
        """
        return {
            "unique_id": self.unique_id,
            "creation_date": self.creation_date.isoformat(),
            "last_updated": self.last_updated.isoformat()
        }

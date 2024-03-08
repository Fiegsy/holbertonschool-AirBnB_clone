#!/usr/bin/python3
"""User class module"""

from models.base_model import BaseModel

class User(BaseModel):
    """Defines the User class which inherits from BaseModel

    Attributes:
        email (str): User email
        password (str): User password
        first_name (str): User's first name
        last_name (str): User's last name
    """

    def __init__(self, email="", password="", first_name="", last_name="", **kwargs):
        """Initialize User instance"""
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

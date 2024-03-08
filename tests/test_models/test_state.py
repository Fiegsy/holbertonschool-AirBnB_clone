#!/usr/bin/python3
"""Unit tests for the State class"""


import unittest
from models.state import State


class TestStateAttributes(unittest.TestCase):
    """Test case for State class attributes"""

    def test_default_name(self):
        """Test default name attribute"""
        state = State()
        self.assertEqual(state.name, "")

    def test_custom_name(self):
        """Test setting a custom name"""
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_custom_name_assignment(self):
        """Test assigning a custom name"""
        state = State()
        state.name = "Texas"
        self.assertEqual(state.name, "Texas")


class TestStateMethods(unittest.TestCase):
    """Test case for State class methods"""

    def test_state_representation(self):
        """Test the __str__ method"""
        state = State(name="New York")
        self.assertEqual(str(state), "<State: New York>")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        state = State(name="Florida")
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['name'], "Florida")
        self.assertTrue(all(key in state_dict.keys() for key in ['__class__', 'id', 'created_at', 'updated_at', 'name']))


if __name__ == '__main__':
    unittest.main()

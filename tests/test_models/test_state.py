#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """State class test"""

    @classmethod
    def setUpClass(cls):
        cls.state_instance = State()
        cls.state_instance.name = "Betty"

    @classmethod
    def tearDownClass(cls):
        del cls.state_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_state(self):
        """Test for PEP8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models.state.py'])
        self.assertEqual(result.total_errors, 0, 'Fix PEP8')

    def test_state_attributes(self):
        """State class attributes test"""
        self.assertTrue('name' in State.__dict__)

    def test_save_state(self):
        """Save State details"""
        BaseModel.save(State)
        self.assertNotEqual(base.created_at, BaseModel.save(State))

    def test_state_attribute_type(self):
        """Test attribute data type"""
        self.assertIsInstance(State.name, str)

    def test_state_instance(self):
        """Test instance"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_docs(self):
        """Documentation in the State class"""
        self.assertIsNotNone(State.__doc__)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """City class test"""

    @classmethod
    def setUpClass(cls):
        cls.city_instance = City()
        cls.city_instance.name = "Betty"
        cls.city_instance.state_id = "Vince"

    @classmethod
    def tearDownClass(cls):
        del cls.city_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_city(self):
        """Test for PEP8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, 'Fix PEP8')

    def test_city_attributes(self):
        """City class attributes test"""
        self.assertTrue("name" in City.__dict__)
        self.assertTrue("state_id" in City.__dict__)

    def test_save_city(self):
        """Save city details"""
        BaseModel.save(City)
        self.assertNotEqual(base.created_at, BaseModel.save(City))

    def test_city_attribute_types(self):
        """Test attribute data types"""
        self.assertTrue(isinstance(City.state_id, str))
        self.assertTrue(isinstance(City.name, str))

    def test_city_instance(self):
        """Test instance"""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_docs(self):
        """Documentation in the City class"""
        self.assertIsNotNone(City.__doc__)

if __name__ == "__main__":
    unittest.main()

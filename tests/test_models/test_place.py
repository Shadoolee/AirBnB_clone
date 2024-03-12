#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """Place class test"""

    @classmethod
    def setUpClass(cls):
        cls.place_instance = Place()
        cls.place_instance.city_id = "Betty"
        cls.place_instance.user_id = "Vince"
        cls.place_instance.name = "vinceoludare"
        cls.place_instance.description = "test loading"
        cls.place_instance.number_rooms = 0
        cls.place_instance.number_bathrooms = 0
        cls.place_instance.max_guest = 0
        cls.place_instance.price_by_night = 0.0
        cls.place_instance.latitude = 6.6
        cls.place_instance.longitude = 0.12
        cls.place_instance.amenity_ids = ["121", 123]

    @classmethod
    def tearDownClass(cls):
        del cls.place_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_place(self):
        """Test for PEP8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, 'Fix PEP8')

    def test_place_attributes(self):
        """Place class attributes test"""
        self.assertTrue('city_id' in Place.__dict__)
        self.assertTrue("user_id" in Place.__dict__)
        self.assertTrue("name" in Place.__dict__)
        self.assertTrue("description" in Place.__dict__)
        self.assertTrue("number_rooms" in Place.__dict__)
        self.assertTrue("number_bathrooms" in Place.__dict__)
        self.assertTrue("max_guest" in Place.__dict__)
        self.assertTrue("price_by_night" in Place.__dict__)
        self.assertTrue("latitude" in Place.__dict__)
        self.assertTrue("longitude" in Place.__dict__)
        self.assertTrue("amenity_ids" in Place.__dict__)

    def test_save_place(self):
        """Save Place details"""
        BaseModel.save(Place)
        self.assertNotEqual(base.created_at, BaseModel.save(Place))

    def test_place_attribute_types(self):
        """Test attribute data types"""
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, float)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

    def test_place_instance(self):
        """Test instance"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_docs(self):
        """Documentation in the Place class"""
        self.assertIsNotNone(Place.__doc__)

if __name__ == "__main__":
    unittest.main()

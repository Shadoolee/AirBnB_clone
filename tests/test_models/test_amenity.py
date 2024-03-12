#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_amenity(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_attributes_present(self):
        self.assertTrue("name" in Amenity.__dict__)

    def test_save_method_updates_created_at(self):
        initial_created_at = self.amenity.created_at
        BaseModel.save(self.amenity)
        self.assertNotEqual(initial_created_at, self.amenity.created_at)

    def test_attribute_data_type(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_instance_creation(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_documentation_present(self):
        self.assertIsNotNone(Amenity.__doc__)

if __name__ == "__main__":
    unittest.main()

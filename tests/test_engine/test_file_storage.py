#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        del self.storage
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation_no_args(self):
        self.assertEqual(type(self.storage), FileStorage)

    def test_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        self.assertEqual(str, type(self.storage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        self.assertEqual(dict, type(self.storage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    def setUp(self):
        self.storage = FileStorage()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        self.storage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(self.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        self.storage.new(bm)
        self.storage.new(us)
        self.storage.new(st)
        self.storage.new(pl)
        self.storage.new(cy)
        self.storage.new(am)
        self.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, self.storage.all().keys())
        self.assertIn(bm, self.storage.all().values())
        self.assertIn("User." + us.id, self.storage.all().keys())
        self.assertIn(us, self.storage.all().values())
        self.assertIn("State." + st.id, self.storage.all().keys())
        self.assertIn(st, self.storage.all().values())
        self.assertIn("Place." + pl.id, self.storage.all().keys())
        self.assertIn(pl, self.storage.all().values())
        self.assertIn("City." + cy.id, self.storage.all().keys())
        self.assertIn(cy, self.storage.all().values())
        self.assertIn("Amenity." + am.id, self.storage.all().keys())
        self.assertIn(am, self.storage.all().values())
        self.assertIn("Review." + rv.id, self.storage.all().keys())
        self.assertIn(rv, self.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            self.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            self.storage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        self.storage.new(bm)
        self.storage.new(us)
        self.storage.new(st)
        self.storage.new(pl)
        self.storage.new(cy)
        self.storage.new(am)
        self.storage.new(rv)
        self.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        self.storage.new(bm)
        self.storage.new(us)
        self.storage.new(st)
        self.storage.new(pl)
        self.storage.new(cy)
        self.storage.new(am)
        self.storage.new(rv)
        self.storage.save()
        self.storage.reload()
        objs = self.storage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, self.storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.reload(None)

if __name__ == "__main__":
    unittest.main()

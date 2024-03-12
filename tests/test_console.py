#!/usr/bin/python3
"""Defines unittests for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import os
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter"""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def tearDown(self):
        storage.reload()

    def assert_output_equal(self, expected_output):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(self.command))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_missing_class(self):
        correct = "** class name missing **"
        self.command = "show"
        self.assert_output_equal(correct)

    def test_show_invalid_class(self):
        correct = "** class doesn't exist **"
        self.command = "show MyModel"
        self.assert_output_equal(correct)

    def test_show_missing_id_space_notation(self):
        correct = "** instance id missing **"
        self.command = "show BaseModel"
        self.assert_output_equal(correct)

    def test_show_missing_id_dot_notation(self):
        correct = "** instance id missing **"
        self.command = "BaseModel.show()"
        self.assert_output_equal(correct)

    def test_show_no_instance_found_space_notation(self):
        correct = "** no instance found **"
        self.command = "show BaseModel 1"
        self.assert_output_equal(correct)

    def test_show_no_instance_found_dot_notation(self):
        correct = "** no instance found **"
        self.command = "BaseModel.show(1)"
        self.assert_output_equal(correct)

    def test_show_objects_space_notation(self):
        classes = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"create {class_name}"
                self.assertFalse(self.hbnb_cmd.onecmd(self.command))
                test_id = storage.all()[f"{class_name}.1"].id

                self.command = f"show {class_name} {test_id}"
                obj = storage.all()[f"{class_name}.{test_id}"]
                self.assert_output_equal(obj.__str__())

    def test_show_objects_dot_notation(self):
        classes = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"create {class_name}"
                self.assertFalse(self.hbnb_cmd.onecmd(self.command))
                test_id = storage.all()[f"{class_name}.1"].id

                self.command = f"{class_name}.show({test_id})"
                obj = storage.all()[f"{class_name}.{test_id}"]
                self.assert_output_equal(obj.__str__())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def tearDown(self):
        storage.reload()

    def assert_output_equal(self, expected_output):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(self.command))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_missing_class(self):
        correct = "** class name missing **"
        self.command = "destroy"
        self.assert_output_equal(correct)

    def test_destroy_invalid_class(self):
        correct = "** class doesn't exist **"
        self.command = "destroy MyModel"
        self.assert_output_equal(correct)

    def test_destroy_id_missing_space_notation(self):
        correct = "** instance id missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"destroy {class_name}"
                self.assert_output_equal(correct)

    def test_destroy_id_missing_dot_notation(self):
        correct = "** instance id missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"{class_name}.destroy()"
                self.assert_output_equal(correct)

    def test_destroy_invalid_id_space_notation(self):
        correct = "** no instance found **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"destroy {class_name} 1"
                self.assert_output_equal(correct)

    def test_destroy_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"{class_name}.destroy(1)"
                self.assert_output_equal(correct)

    def test_destroy_objects_space_notation(self):
        classes = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"create {class_name}"
                self.assertFalse(self.hbnb_cmd.onecmd(self.command))
                test_id = storage.all()[f"{class_name}.1"].id

                self.command = f"destroy {class_name} {test_id}"
                obj = storage.all()[f"{class_name}.{test_id}"]
                self.assertNotIn(obj, storage.all())

    def test_destroy_objects_dot_notation(self):
        classes = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"create {class_name}"
                self.assertFalse(self.hbnb_cmd.onecmd(self.command))
                test_id = storage.all()[f"{class_name}.1"].id

                self.command = f"{class_name}.destroy({test_id})"
                obj = storage.all()[f"{class_name}.{test_id}"]
                self.assertNotIn(obj, storage.all())


class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for testing all of the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def tearDown(self):
        storage.reload()

    def assert_output_equal(self, expected_output):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(self.command))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_all_invalid_class(self):
        correct = "** class doesn't exist **"
        self.command = "all MyModel"
        self.assert_output_equal(correct)

    def test_all_objects_space_notation(self):
        classes = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
        with patch("sys.stdout", new=StringIO()) as output:
            for class_name in classes:
                self.assertFalse(self.hbnb_cmd.onecmd(f"create {class_name}"))
            self.command = "all"
            for class_name in classes:
                with self.subTest(class_name=class_name):
                    self.assertIn(class_name, output.getvalue().strip())

    def test_all_objects_dot_notation(self):
        classes = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
        with patch("sys.stdout", new=StringIO()) as output:
            for class_name in classes:
                self.assertFalse(self.hbnb_cmd.onecmd(f"create {class_name}"))
            self.command = ".all()"
            for class_name in classes:
                with self.subTest(class_name=class_name):
                    self.assertIn(class_name, output.getvalue().strip())

    def test_all_single_object_space_notation(self):
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        with patch("sys.stdout", new=StringIO()) as output:
            for class_name in classes:
                self.assertFalse(self.hbnb_cmd.onecmd(f"create {class_name}"))
            for class_name in classes:
                with self.subTest(class_name=class_name):
                    self.command = f"all {class_name}"
                    self.assertIn(class_name, output.getvalue().strip())
                    self.assertNotIn("BaseModel", output.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def tearDown(self):
        storage.reload()

    def assert_output_equal(self, expected_output):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(self.command))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_missing_class(self):
        correct = "** class name missing **"
        self.command = "update"
        self.assert_output_equal(correct)

    def test_update_invalid_class(self):
        correct = "** class doesn't exist **"
        self.command = "update MyModel"
        self.assert_output_equal(correct)

    def test_update_missing_id(self):
        correct = "** instance id missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"update {class_name}"
                self.assert_output_equal(correct)

    def test_update_invalid_id(self):
        correct = "** no instance found **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.command = f"update {class_name} 1"
                self.assert_output_equal(correct)

    def test_update_missing_attr_name(self):
        correct = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                self.assertFalse(self.hbnb_cmd.onecmd(f"create {class_name}"))
                test_id = storage.all()[f"{class_name}.1"].id
                self.command = f"update {class_name} {test_id}"
                self.assert_output_equal(correct)


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def tearDown(self):
        storage.reload()

    def assert_output_equal(self, expected_output):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(self.command))
            self.assertEqual(expected_output, output.getvalue().strip())

    def create_instance_and_get_id(self, class_name):
        with patch("sys.stdout", new=StringIO()) as output:
            self.hbnb_cmd.onecmd(f"create {class_name}")
            return output.getvalue().strip()

    def test_update_missing_attr_name_space_notation(self):
        correct = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                test_id = self.create_instance_and_get_id(class_name)
                self.command = f"{class_name}.update({{'_id': '{test_id}'}})"
                self.assert_output_equal(correct)

    def test_update_missing_attr_value_space_notation(self):
        correct = "** value missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                test_id = self.create_instance_and_get_id(class_name)
                self.command = f"{class_name}.update({{'_id': '{test_id}', 'attr_name': ''}})"
                self.assert_output_equal(correct)

    def test_update_valid_string_attr_space_notation(self):
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                test_id = self.create_instance_and_get_id(class_name)
                self.command = f"{class_name}.update({{'_id': '{test_id}', 'attr_name': 'attr_value'}})"
                self.assertFalse(self.hbnb_cmd.onecmd(self.command))
                test_dict = storage.all()[f"{class_name}.{test_id}"].__dict__
                self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_missing_attr_name_dot_notation(self):
        correct = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                test_id = self.create_instance_and_get_id(class_name)
                self.command = f"{class_name}.update({{'_id': '{test_id}'}})"
                self.assert_output_equal(correct)

    def test_update_missing_attr_value_dot_notation(self):
        correct = "** value missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                test_id = self.create_instance_and_get_id(class_name)
                self.command = f"{class_name}.update({{'_id': '{test_id}', 'attr_name': ''}})"
                self.assert_output_equal(correct)

    def test_update_valid_string_attr_dot_notation(self):
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with self.subTest(class_name=class_name):
                test_id = self.create_instance_and_get_id(class_name)
                self.command = f"{class_name}.update({{'_id': '{test_id}', 'attr_name': 'attr_value'}})"
                self.assertFalse(self.hbnb_cmd.onecmd(self.command))
                test_dict = storage.all()[f"{class_name}.{test_id}"].__dict__
                self.assertEqual("attr_value", test_dict["attr_name"])
 def test_update_valid_string_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            tId = output.getvalue().strip()
        testCmd = "BaseModel.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            tId = output.getvalue().strip()
        testCmd = "User.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            tId = output.getvalue().strip()
        testCmd = "State.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            tId = output.getvalue().strip()
        testCmd = "City.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            tId = output.getvalue().strip()
        testCmd = "Amenity.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            tId = output.getvalue().strip()
        testCmd = "Review.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_int_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} max_guest 98".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_int_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, max_guest, 98)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_float_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} latitude 7.2".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_float_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, latitude, 7.2)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_dictionary_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "update BaseModel {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        testCmd = "update User {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testId = output.getvalue().strip()
        testCmd = "update State {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testId = output.getvalue().strip()
        testCmd = "update City {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testId = output.getvalue().strip()
        testCmd = "update Amenity {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testId = output.getvalue().strip()
        testCmd = "update Review {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            testId = output.getvalue().strip()
        testCmd = "BaseModel.update({}".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            testId = output.getvalue().strip()
        testCmd = "User.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            testId = output.getvalue().strip()
        testCmd = "State.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            testId = output.getvalue().strip()
        testCmd = "City.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            testId = output.getvalue().strip()
        testCmd = "Amenity.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            testId = output.getvalue().strip()
        testCmd = "Review.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_int_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_int_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_float_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_update_valid_dictionary_with_float_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])


class TestHBNBCommand_count(unittest.TestCase):
    """Unittests for testing count method of HBNB comand interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()

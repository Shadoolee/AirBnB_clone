import pep8
import os
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """User class test"""

    @classmethod
    def setUpClass(cls):
        cls.user_instance = User()
        cls.user_instance.first_name = "Betty"
        cls.user_instance.last_name = "Vince"
        cls.user_instance.email = "vinceoludare@gmail.com"
        cls.user_instance.password = "2324f"

    @classmethod
    def tearDownClass(cls):
        del cls.user_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_user(self):
        """Test for PEP8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, 'Check PEP8')

    def test_user_attributes(self):
        """User class attributes test"""
        self.assertTrue('email' in User.__dict__)
        self.assertTrue("password" in User.__dict__)
        self.assertTrue("first_name" in User.__dict__)
        self.assertTrue("last_name" in User.__dict__)

    def test_save_user(self):
        """Save user details"""
        BaseModel.save(User)
        self.assertNotEqual(base.created_at, BaseModel.save(User))

    def test_user_attribute_type(self):
        """Test attribute data type"""
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.email, str)

    def test_user_instance(self):
        """Test instance"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_docs(self):
        """Documentation in the User class"""
        self.assertIsNotNone(User.__doc__)

if __name__ == "__main__":
    unittest.main()

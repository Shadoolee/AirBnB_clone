#!/usr/bin/python3
import pep8
import os
import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """Review class test"""

    @classmethod
    def setUpClass(cls):
        cls.review_instance = Review()
        cls.review_instance.place_id = "Betty"
        cls.review_instance.user_id = "vince"
        cls.review_instance.text = "getting a successful text"

    @classmethod
    def tearDownClass(cls):
        del cls.review_instance
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_review(self):
        """Test for PEP8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models.review.py'])
        self.assertEqual(result.total_errors, 0, 'Fix PEP8')

    def test_review_attributes(self):
        """Review class attributes test"""
        self.assertTrue('place_id' in Review.__dict__)
        self.assertTrue("user_id" in Review.__dict__)
        self.assertTrue("text" in Review.__dict__)

    def test_save_review(self):
        """Save Review details"""
        BaseModel.save(Review)
        self.assertNotEqual(base.created_at, BaseModel.save(Review))

    def test_review_attribute_types(self):
        """Test attribute data types"""
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_review_instance(self):
        """Test instance"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_docs(self):
        """Documentation in the Review class"""
        self.assertIsNotNone(Review.__doc__)

if __name__ == "__main__":
    unittest.main()

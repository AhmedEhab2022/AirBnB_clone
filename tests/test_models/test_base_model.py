#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instantiation(self):
        """Tests instantiation of BaseModel class"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(issubclass(type(bm), BaseModel))

    def test_id(self):
        """Tests id attribute"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertIsInstance(bm.id, str)

    def test_created_at(self):
        """Tests created_at attribute"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertIsInstance(bm.created_at, datetime)

    def test_updated_at(self):
        """Tests updated_at attribute"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        """Tests save method"""
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_str(self):
        """Tests __str__ method"""
        bm = BaseModel()
        bm_str = bm.__str__()
        self.assertEqual(bm_str,
                         "[BaseModel] ({}) <{}>".format(bm.id, bm.__dict__))

    def test_to_dict(self):
        """Tests to_dict method"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)

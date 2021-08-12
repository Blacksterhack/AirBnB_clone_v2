#!/usr/bin/python3
"""Module for test User class"""
import unittest
import json
import pep8
import datetime

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test User class implementation"""

    def test_doc_module(self):
        """Module documentation"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """Test that models/user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)


if __name__ == '__main__':
    unittest.main()

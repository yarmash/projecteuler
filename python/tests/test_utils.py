"""
This module contains tests for utils.

To run the tests execute:
$ nosetests -v tests/test_utils.py
or
$ python -m unittest -v tests/test_utils.py
"""

import unittest
import utils


class TestUtils(unittest.TestCase):

    def test_arithmetic_series(self):
        self.assertEqual(utils.arithmetic_series(1, 100, 100), 5050)
        self.assertEqual(utils.arithmetic_series(2, 100, 50), 2550)

    def test_is_square(self):
        self.assertTrue(utils.is_square(4))
        self.assertFalse(utils.is_square(8))
        x = 12345678987654321234567 ** 2
        self.assertTrue(utils.is_square(x))
        self.assertFalse(utils.is_square(x + 2))

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

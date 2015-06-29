"""
This module contains tests for utils.

To run the tests execute:
$ nosetests -v tests/test_utils.py
or
$ python -m unittest -v tests/test_utils.py
"""

import unittest

from utils import (
    arithmetic_series,
    is_pandigital,
    is_pentagonal,
    is_prime,
    is_square,
    is_triangular_number,
    nth_pentagonal,
    nth_triangle,
)


class TestUtils(unittest.TestCase):
    def test_arithmetic_series(self):
        self.assertEqual(arithmetic_series(1, 100, 100), 5050)
        self.assertEqual(arithmetic_series(2, 100, 50), 2550)

    def test_is_pentagonal(self):
        self.assertTrue(is_pentagonal(1))
        self.assertFalse(is_pentagonal(2))
        self.assertTrue(is_pentagonal(5))
        self.assertFalse(is_pentagonal(15))

        n = 10**15
        p = nth_pentagonal(n)
        self.assertTrue(is_pentagonal(p))
        self.assertFalse(is_pentagonal(p + 2))

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(15485863))

    def test_is_square(self):
        self.assertTrue(is_square(4))
        self.assertFalse(is_square(8))
        x = 12345678987654321234567 ** 2
        self.assertTrue(is_square(x))
        self.assertFalse(is_square(x + 2))

    def test_is_triangular_number(self):
        self.assertTrue(is_triangular_number(1))
        self.assertFalse(is_triangular_number(2))
        n = 10**15
        t = nth_triangle(n)
        self.assertTrue(is_triangular_number(t))
        self.assertFalse(is_triangular_number(t + 2))

    def test_is_pandigital(self):
        # The first pandigital number
        self.assertTrue(is_pandigital(1023456789, start=0, end=9))
        # The first zeroless pandigital number
        self.assertTrue(is_pandigital(123456789, start=1, end=9))
        # A pandigital number w/ redundant digits
        self.assertTrue(is_pandigital(1223334444555567890, start=0, end=9))
        # The smallest pandigital palindromic number in base 10
        self.assertTrue(is_pandigital(1023456789876543201, start=0, end=9))

        self.assertTrue(is_pandigital(12345678987654321, start=1, end=9))
        self.assertTrue(is_pandigital(10234, start=0, end=4))
        self.assertTrue(is_pandigital(456789, start=4, end=9))
        self.assertFalse(is_pandigital(123456789, start=0, end=9))
        self.assertFalse(is_pandigital(1023456789, start=1, end=9))
        self.assertFalse(is_pandigital(102345, start=0, end=4))

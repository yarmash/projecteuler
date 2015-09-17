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
    exp_by_squaring,
    is_pandigital,
    is_pentagonal,
    is_prime,
    is_square,
    is_triangular_number,
    isqrt,
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
        self.assertTrue(is_pandigital(923456781))
        self.assertFalse(is_pandigital(12345678))
        self.assertFalse(is_pandigital(102345678))
        self.assertFalse(is_pandigital(1023456789))

    def test_exp_by_squaring(self):
        for num, p in ((2, 3), (10, 10), (1234, 5678)):
            self.assertEqual(exp_by_squaring(num, p), pow(num, p))

    def test_isqrt(self):
        data = (
            (0, 0), (1, 1), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2), (7, 2),
            (8, 2), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3),
            (15, 3), (16, 4), (17, 4), (18, 4), (19, 4), (20, 4), (21, 4),
            (22, 4), (23, 4), (24, 4), (25, 5), (26, 5), (27, 5), (28, 5),
            (29, 5), (30, 5), (31, 5), (32, 5), (33, 5), (34, 5), (35, 5),
            (36, 6), (37, 6), (38, 6), (39, 6), (40, 6), (99, 9), (100, 10),
            (101, 10), (289, 17), (65535, 255), (65536, 256), (65537, 256),
            (1073741823, 32767), (1073741824, 32768), (1073741825, 32768),
            (2147483648, 46340), (4294967295, 65535))

        for num, root in data:
            self.assertEqual(isqrt(num), root,
                             "isqrt({}) != {}".format(num, root))

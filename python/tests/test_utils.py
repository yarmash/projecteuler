"""This module contains tests for the utils module."""

import unittest
from itertools import islice

from utils import (  # isort:skip
    arithmetic_series,
    hexagonal_numbers,
    is_palindrome,
    is_pandigital,
    is_pentagonal,
    is_prime,
    is_square,
    nth_pentagonal,
    num_of_divisors,
    sum_digits,
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

    def test_hexagonal_numbers(self):
        self.assertEqual(list(islice(hexagonal_numbers(), 20)),
                         [1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276,
                          325, 378, 435, 496, 561, 630, 703, 780])

    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(923456781))
        self.assertFalse(is_pandigital(12345678))
        self.assertFalse(is_pandigital(102345678))
        self.assertFalse(is_pandigital(1023456789))

    def test_sum_digits(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(1), 1)
        self.assertEqual(sum_digits(1000), 1)
        self.assertEqual(sum_digits(1234567890), 45)

    def test_num_of_divisors(self):
        self.assertEqual([num_of_divisors(x) for x in range(1, 17)],
                         [1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(1))
        self.assertFalse(is_palindrome(10))
        self.assertTrue(is_palindrome(101))
        self.assertFalse(is_palindrome(int("10", base=2), base=2))
        self.assertTrue(is_palindrome(int("101", base=2), base=2))
        self.assertFalse(is_palindrome(int("123", base=4), base=4))
        self.assertTrue(is_palindrome(int("12321", base=4), base=4))

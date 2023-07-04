#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regList(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsortList(self):
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-2, -1, -5, -3]), -1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        self.assertEqual(max_integer([2.3, 6.7, 6.36, 0.5]), 6.7)

    def test_datatype(self):
        with self.assertRaises(TypeError):
            max_integer([2, 4, '3', 1])

if __name__ == "__main__":
    unitest.main()

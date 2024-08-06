#!/usr/bin/python3


# tests/test_your_code.py

import unittest
from your_code import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53975)

    def test_circumference(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.circumference(), 31.4159)

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

if __name__ == '__main__':
    unittest.main()


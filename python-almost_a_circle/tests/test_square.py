#!/usr/bin/python3


import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_square_init(self):
        s = Square(1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_str(self):
        s = Square(5, 2, 3, 9)
        self.assertEqual(str(s), "[Square] (9) 2/3 - 5")

    def test_square_to_dictionary(self):
        s = Square(10, 2, 1, 9)
        self.assertEqual(s.to_dictionary(), {
            'id': s.id,
            'size': 10,
            'x': 2,
            'y': 1
        })

    def test_square_update_args(self):
        s = Square(10)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_square_update_kwargs(self):
        s = Square(10)
        s.update(id=89, size=1)
        self.assert


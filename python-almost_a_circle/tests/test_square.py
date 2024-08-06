
import unittest
from square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        # Reset state before each test
        Square._Base__nb_objects = 0

    def test_square_id_auto(self):
        s1 = Square(1)
        s2 = Square(1)
        self.assertEqual(s1.id + 1, s2.id)

    def test_square_id_given(self):
        s1 = Square(1, id=89)
        self.assertEqual(s1.id, 89)

    def test_square_invalid_size(self):
        with self.assertRaises(ValueError):
            Square(-1)
        s = Square(1)
        with self.assertRaises(ValueError):
            s.size = -1

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_update(self):
        s1 = Square(10, 2, 1, 1)
        s1.update(89)
        self.assertEqual(s1.id, 89)
        s1.update(size=4)
        self.assertEqual(s1.size, 4)

if __name__ == '__main__':
    unittest.main()



import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Reset state before each test
        Rectangle._Base__nb_objects = 0

    def test_save_to_file(self):
        r1 = Rectangle(1, 2, 0, 0, 1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    # Add more tests for Rectangle

if __name__ == '__main__':
    unittest.main()


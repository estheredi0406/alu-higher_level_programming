#!/usr/bin/python3


import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_init(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rectangle_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_rectangle_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_display(self):
        r = Rectangle(2, 3)
        r.display()

    def test_rectangle_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.to_dictionary(), {
            'id': r.id,
            'width': 10,
            'height': 2,
            'x': 1,
            'y': 9
        })

    def test_rectangle_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_rectangle_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_rectangle_create(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_save_to_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_load_from_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles), 1)
        self.assertIsInstance(list_rectangles[0], Rectangle)

if __name__ == '__main__':
    unittest.main()


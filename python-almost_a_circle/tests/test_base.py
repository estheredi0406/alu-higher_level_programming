#!/usr/bin/python3


import unittest
from base import Base

class TestBase(unittest.TestCase):
    def test_base_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_base_id_given(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])

if __name__ == '__main__':
    unittest.main()


import unittest

from advent.item import Item
from advent.priorities import Priorities


class ItemTests(unittest.TestCase):
    def test_create(self):
        self.assertEqual(Item('a').priority, 1)
        self.assertEqual(Item('z').priority, 26)
        self.assertEqual(Item('A').priority, 27)
        self.assertEqual(Item('Z').priority, 52)

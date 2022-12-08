import unittest

from advent.tree import Tree


class TreeTests(unittest.TestCase):
    def test_conditions(self):
        self.assertEqual(Tree(1), Tree(1), 'Trees should be equal')
        self.assertGreater(Tree(9), Tree(1), 'First tree should be taller')
        self.assertLess(Tree(3), Tree(8), 'First tree should be smaller')

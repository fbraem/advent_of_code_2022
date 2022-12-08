import unittest

from advent.forest import Forest
from advent.tree import Tree


class ForestTests(unittest.TestCase):
    def test_add_row(self):
        forest = Forest()
        forest.add_row(Tree(1), Tree(3), Tree(4))
        forest.add_row(Tree(4), Tree(5), Tree(6))
        self.assertEqual(forest.row_count, 2, 'The forest should have 2 rows')

    def test_is_visible(self):
        forest = Forest()
        forest.add_row_from_string('30373')
        forest.add_row_from_string('25512')
        forest.add_row_from_string('65332')
        forest.add_row_from_string('33549')
        forest.add_row_from_string('35390')

        self.assertEqual(forest.get_tree(1, 1), Tree(5), 'The tree should be 5 high')
        self.assertTrue(forest.is_tree_visible(1, 1), 'The tree should be visible')
        self.assertTrue(forest.is_tree_visible(1, 2), 'The tree should be visible')
        self.assertTrue(forest.is_tree_visible(2, 1), 'The tree should be visible')
        self.assertFalse(forest.is_tree_visible(2, 2), 'The tree should not be visible')
        self.assertTrue(forest.is_tree_visible(2, 3), 'The tree should be visible')
        self.assertTrue(forest.is_tree_visible(3, 2), 'The tree should be visible')
        self.assertFalse(forest.is_tree_visible(3, 1), 'The tree should not be visible')
        self.assertFalse(forest.is_tree_visible(3, 3), 'The tree should not be visible')

        self.assertEqual(forest.count_visible_trees(), 21, 'There should be 16 trees visible')

    def test_get_scenic_score(self):
        forest = Forest()
        forest.add_row_from_string('30373')
        forest.add_row_from_string('25512')
        forest.add_row_from_string('65332')
        forest.add_row_from_string('33549')
        forest.add_row_from_string('35390')

        self.assertEqual(4, forest.get_scenic_score(1, 2), 'Scenic score should be 4')
        self.assertEqual(8, forest.get_scenic_score(3, 2), 'Scenic score should be 8')

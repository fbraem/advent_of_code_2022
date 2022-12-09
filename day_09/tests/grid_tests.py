import unittest

from advent.grid import Grid
from advent.rope import Rope


class GridTests(unittest.TestCase):
    def test_grid(self):
        rope = Rope((5, 1), (5, 1))
        grid = Grid(5, 6, rope)

        self.assertEqual(1, grid.get_visited(5, 1), 'The start position should be visited')

        grid.move_rope('R', 4)
        grid.move_rope('U', 4)
        grid.move_rope('L', 3)
        grid.move_rope('D', 1)
        grid.move_rope('R', 4)
        grid.move_rope('D', 1)
        grid.move_rope('L', 5)
        grid.move_rope('R', 2)

        self.assertEqual(13, grid.number_of_visits, 'There should be 13 visits')

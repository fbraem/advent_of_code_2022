import unittest

from advent.grid import Grid
from advent.rope import Rope


class GridTests(unittest.TestCase):
    def test_grid(self):
        rope = Rope((5, 1), (5, 1))
        grid = Grid(rope)

        self.assertTrue(grid.is_visited((5, 1)), 'The start position should be visited')

        grid.move_rope('R', 4)
        grid.move_rope('U', 4)
        grid.move_rope('L', 3)
        grid.move_rope('D', 1)
        grid.move_rope('R', 4)
        grid.move_rope('D', 1)
        grid.move_rope('L', 5)
        grid.move_rope('R', 2)

        self.assertEqual(13, grid.number_of_visits, 'There should be 13 visits')

    def test_grid_multiple_knots(self):
        start_knot = (5, 1)
        rope = Rope(*(start_knot,) * 10)

        grid = Grid(rope)
        grid.move_rope('R', 4)
        grid.move_rope('U', 4)
        grid.move_rope('L', 3)
        grid.move_rope('D', 1)
        grid.move_rope('R', 4)
        grid.move_rope('D', 1)
        grid.move_rope('L', 5)
        grid.move_rope('R', 2)

        self.assertEqual(1, grid.number_of_visits, 'The tail did not move, so it should be 1 visit')

    def test_grid_large_multiple_knots(self):
        start_knot = (16, 12)
        rope = Rope(*(start_knot,) * 10)

        grid = Grid(rope)
        grid.move_rope('R', 5)
        grid.move_rope('U', 8)
        grid.move_rope('L', 8)
        grid.move_rope('D', 3)
        grid.move_rope('R', 17)
        grid.move_rope('D', 10)
        grid.move_rope('L', 25)
        grid.move_rope('U', 20)

        self.assertEqual(36, grid.number_of_visits, 'The tail should have visited 36 positions')

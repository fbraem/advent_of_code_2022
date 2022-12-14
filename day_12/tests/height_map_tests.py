import unittest

from advent.height_map import HeightMap


class HeightMapTests(unittest.TestCase):
    def test_add_row(self):
        height_map = HeightMap()
        height_map.add_row('aaab')
        height_map.add_row('babc')

        self.assertEqual(2, height_map.row_count, 'There should be 2 rows')

    def test_start_end(self):
        height_map = HeightMap()
        height_map.add_row('Saab')
        height_map.add_row('baEc')

        self.assertEqual((0, 0), height_map.start, 'Start should be at position (0, 0)')
        self.assertEqual((1, 2), height_map.end, 'End should be at position (1, 2)')

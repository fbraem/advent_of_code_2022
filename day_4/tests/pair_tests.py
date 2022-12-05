import unittest
from textwrap import dedent
from unittest import mock

from advent.elf import Elf
from advent.pair import Pair
from advent.pairs_importer import PairsImporter

TEST_DATA = dedent("""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""")


class PairTests(unittest.TestCase):
    def test_is_fully_contained(self):
        elf_1 = Elf()
        elf_1.add_section(2, 8)
        elf_2 = Elf()
        elf_2.add_section(3, 7)

        self.assertTrue(Pair(elf_1, elf_2).is_fully_contained(), 'Should have fully contained assignments')

        elf_1 = Elf()
        elf_1.add_section(6, 6)
        elf_2 = Elf()
        elf_2.add_section(4, 6)

        self.assertTrue(Pair(elf_1, elf_2).is_fully_contained(), 'Should have fully contained assignments')

    def test_is_not_fully_contained(self):
        elf_1 = Elf()
        elf_1.add_section(2, 3)
        elf_2 = Elf()
        elf_2.add_section(4, 5)

        self.assertFalse(Pair(elf_1, elf_2).is_fully_contained(), 'Should have no fully contained assignments')

        elf_1 = Elf()
        elf_1.add_section(2, 6)
        elf_2 = Elf()
        elf_2.add_section(4, 8)

        self.assertFalse(Pair(elf_1, elf_2).is_fully_contained(), 'Should have no fully contained assignments')

    @mock.patch("builtins.open", mock.mock_open(read_data=TEST_DATA))
    def test_with_importer(self):
        importer = PairsImporter()
        importer.read_file('test')

        count = 0
        for pair in importer.pairs:
            if pair.is_fully_contained():
                count += 1
        self.assertEqual(count, 2, "There should be 2 fully contained pairs")

    def test_overlap(self):
        elf_1 = Elf()
        elf_1.add_section(5, 7)
        elf_2 = Elf()
        elf_2.add_section(7, 9)

        self.assertEqual(Pair(elf_1, elf_2).get_overlaps(), {7}, 'The overlap should contain 7')

        elf_1 = Elf()
        elf_1.add_section(6, 6)
        elf_2 = Elf()
        elf_2.add_section(4, 6)

        self.assertEqual(Pair(elf_1, elf_2).get_overlaps(), {6}, 'The overlap should contain 6')

        elf_1 = Elf()
        elf_1.add_section(2, 6)
        elf_2 = Elf()
        elf_2.add_section(4, 8)

        self.assertEqual(Pair(elf_1, elf_2).get_overlaps(), {4, 5, 6}, 'The overlap should contain 4, 5, 6')

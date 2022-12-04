import unittest

from advent.group import Group
from advent.rucksack import Rucksack


class GroupTests(unittest.TestCase):
    def test_group_badge(self):
        group = Group(
            Rucksack('vJrwpWtwJgWrhcsFMMfFFhFp'),
            Rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'),
            Rucksack('PmmdzqPrVvPwwTWBwg')
        )
        badge = group.find_badge()
        self.assertIsNotNone(badge, 'There should be a badge')
        self.assertEqual(badge.char, 'r', 'The badge should be r')

        group = Group(
            Rucksack('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'),
            Rucksack('ttgJtRGJQctTZtZT'),
            Rucksack('CrZsJsPPZsGzwwsLwLmpwMDw'),
        )
        badge = group.find_badge()
        self.assertIsNotNone(badge, 'There should be a badge')
        self.assertEqual(badge.char, 'Z', 'The badge should be Z')

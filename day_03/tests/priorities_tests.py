import unittest

from advent.priorities import Priorities


class PrioritiesTests(unittest.TestCase):
    def test_priorities(self):
        priorities = Priorities()

        self.assertEqual(priorities.get('a'), 1)
        self.assertEqual(priorities.get('z'), 26)
        self.assertEqual(priorities.get('A'), 27)
        self.assertEqual(priorities.get('Z'), 52)

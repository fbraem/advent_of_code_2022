import unittest

from advent.rucksack import Rucksack


class RucksackTests(unittest.TestCase):
    def test_fill(self):
        rucksack = Rucksack()
        rucksack.fill('vJrwpWtwJgWrhcsFMMfFFhFp')
        self.assertEqual(len(rucksack.compartments), 2)
        self.assertEqual(
            len(rucksack.compartments[0]),
            len(rucksack.compartments[1]),
            'The number of items in each compartment must be the same'
        )
        self.assertEqual(
            rucksack.compartments[0][-1].char,
            'r',
            'The last item of the first compartment must be r'
        )
        self.assertEqual(
            rucksack.compartments[1][-1].char,
            'p',
            'The last item of the second compartment must be p'
        )

    def test_find_shared_item(self):
        rucksack = Rucksack()
        rucksack.fill('vJrwpWtwJgWrhcsFMMfFFhFp')
        shared = rucksack.find_shared_item()
        self.assertIsNotNone(shared, 'There should be a shared item')
        self.assertEqual(shared.char, 'p', 'The shared item should be p')
        self.assertEqual(shared.priority, 16, 'The shared item should have priority 16')

        rucksack.fill('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')
        # print(rucksack.compartments)
        shared = rucksack.find_shared_item()
        self.assertIsNotNone(shared, 'There should be a shared item')
        self.assertEqual(shared.char, 'L', 'The shared item should be L')
        self.assertEqual(shared.priority, 38, 'The shared item should have priority 38')

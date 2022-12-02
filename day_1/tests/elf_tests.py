import unittest

from advent.elf import Elf
from advent.food import Food


class ElfTest(unittest.TestCase):
    def test_add_food(self):
        elf = Elf()
        elf.add_food(Food(1000), Food(2000), Food(3000))

        self.assertEqual(elf.carried_calories, 6000)

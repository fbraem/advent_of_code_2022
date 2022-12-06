import unittest

from advent.elf import Elf


class ElfTests(unittest.TestCase):
    def test_add_section(self):
        elf = Elf()
        elf.add_section(2, 4)
        self.assertEqual(elf.sections, [2, 3, 4])

        elf = Elf()
        elf.add_section(2, 8)
        self.assertEqual(elf.sections, [2, 3, 4, 5, 6, 7, 8])

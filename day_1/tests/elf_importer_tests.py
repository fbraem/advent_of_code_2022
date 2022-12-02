import unittest

from advent.elf_importer import ElfImporter


class ElfImporterTest(unittest.TestCase):
    def test_import_file(self):
        importer = ElfImporter()
        importer.read_file('../files/day1_input')

        self.assertGreater(importer.elves.count, 1)
        self.assertEqual(importer.elves.get(0).load_count, 7)

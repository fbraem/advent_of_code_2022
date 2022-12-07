import unittest

from advent.file_system import FileSystem


class FileSystemObjectTests(unittest.TestCase):
    def test_get_size(self):
        fs = FileSystem()
        fs.add_file('b.txt', 14848514)
        fs.add_file('c.dat', 8504156)

        self.assertEqual(fs.current.get_file('b.txt').get_size(), 14848514)
        self.assertEqual(fs.current.get_file('c.dat').get_size(), 8504156)
        self.assertEqual(fs.current.get_size(), 14848514 + 8504156)

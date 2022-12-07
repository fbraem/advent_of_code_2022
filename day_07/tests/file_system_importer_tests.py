import unittest
from unittest import mock

from advent.file_system_importer import FileSystemImporter
from advent.file_system_object import Directory

TEST_DATA = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class FileSystemImporterTests(unittest.TestCase):
    @mock.patch("builtins.open", mock.mock_open(read_data=TEST_DATA))
    def test_import(self):
        fs_importer = FileSystemImporter()
        fs = fs_importer.read_file('test_data')

        fs.reset()
        self.assertEqual(fs.current.get_size(), 48381165, 'The size of the root should be 48381165')
        self.assertIsInstance(fs.cd('a'), Directory, 'This should be a directory')
        self.assertEqual(fs.current.get_size(), 94853, 'The size of a should be 94853')
        self.assertIsInstance(fs.cd('e'), Directory, 'This should be a directory')
        self.assertEqual(fs.current.get_size(), 584, 'The size of e should be 584')

    @mock.patch("builtins.open", mock.mock_open(read_data=TEST_DATA))
    def test_at_most(self):
        fs_importer = FileSystemImporter()
        fs = fs_importer.read_file('test_data')

        fs.reset()

        at_most_dirs = []

        def select_at_most(directory: Directory):
            if directory.get_size() < 100000:
                at_most_dirs.append(directory)

        fs.current.walk(select_at_most)
        dir_names = [directory.name for directory in at_most_dirs]
        self.assertEqual(dir_names, ['a', 'e'], 'Only a and e have at most 100000 bytes')
        total_bytes = sum([directory.get_size() for directory in at_most_dirs])
        self.assertEqual(total_bytes, 95437, 'Total bytes should be 95437')

    @mock.patch("builtins.open", mock.mock_open(read_data=TEST_DATA))
    def test_free_space(self):
        fs_importer = FileSystemImporter()
        fs = fs_importer.read_file('test_data')
        fs.reset()

        min_space = 30000000

        self.assertEqual(fs.free_space, 21618835, 'Free space should be 21618835')

        extra_space = min_space - fs.free_space
        self.assertEqual(extra_space, 8381165, 'At least 8381165 bytes must be freed')

        dir_sizes = {}

        def collect_size(directory: Directory):
            dir_sizes[directory.name] = directory.get_size()

        fs.current.walk(collect_size)

        dir_with_min_size = min([x for x in dir_sizes.values() if x > extra_space])
        self.assertEqual(dir_with_min_size, 24933642, 'The directory to delete should free 24933642 bytes')

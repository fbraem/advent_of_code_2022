from advent.file_system_importer import FileSystemImporter
from advent.file_system_object import Directory


fs_importer = FileSystemImporter()
fs = fs_importer.read_file('./files/day7_input')
fs.reset()

at_most_dirs = []


# We use a function to walk through all directories
# This function will be called for all directories and select the directories
# with at most 100000 bytes.
def select_at_most(directory: Directory):
    if directory.get_size() < 100000:
        at_most_dirs.append(directory)


fs.current.walk(select_at_most)
total_bytes = sum([directory.get_size() for directory in at_most_dirs])
print('Total sizes of directories with at most 100000 bytes:', total_bytes)

disk_space = 70000000
print('Free space:', fs.free_space)
min_space = 30000000
extra_space = min_space - fs.free_space
print('Extra space needed:', extra_space)

# Collect all directories and their sizes
dir_sizes = {}


def collect_size(directory: Directory):
    dir_sizes[directory.name] = directory.get_size()


fs.current.walk(collect_size)
# Search all directories with at least extra_space bytes, and take the smallest
dir_with_min_size = min([x for x in dir_sizes.values() if x > extra_space])
print('The size of the smallest directory to delete is:', dir_with_min_size)

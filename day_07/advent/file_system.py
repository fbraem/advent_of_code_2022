from typing import Optional

from advent.file_system_object import Directory, File

DISK_SPACE = 70000000


class FileSystem:
    def __init__(self):
        self._root = Directory('')
        self._current = self._root

    @property
    def current(self) -> 'Directory':
        return self._current

    def cd(self, directory: str) -> Optional['Directory']:
        match directory:
            case '/':
                self._current = self._root
            case '..':
                self._current = self._current.parent
            case _:
                self._current = self._current.get_directory(directory)

        return self._current

    @property
    def free_space(self):
        return DISK_SPACE - self._root.get_size()

    def add_directory(self, name: str) -> 'Directory':
        return self._current.add_directory(name)

    def add_file(self, name: str, size: int) -> 'File':
        file = File(name, size)
        self._current.add_file(file)
        return file

    def reset(self):
        # Set the current directory back to the root
        self._current = self._root

    def up(self):
        # Set the current directory to its parent
        self._current = self._current.parent

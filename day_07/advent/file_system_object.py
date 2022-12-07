from abc import abstractmethod, ABC
from typing import Optional, Callable


class FileSystemObject(ABC):
    """Base class for a filesystem object.
    """
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_size(self) -> int:
        pass


class File(FileSystemObject):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    def get_size(self) -> int:
        return self._size

    def __str__(self):
        return self._name


class Directory(FileSystemObject):
    def __init__(self, name: str, parent: Optional['Directory'] = None):
        super().__init__(name)
        self._parent = parent
        self._dirs = []
        self._files = []

    @property
    def parent(self) -> 'Directory':
        return self._parent

    @property
    def directories(self) -> list['Directory']:
        return self._dirs.copy()

    def add_file(self, file: File):
        self._files.append(file)

    def add_directory(self, name: str) -> 'Directory':
        directory = Directory(name, self)
        self._dirs.append(directory)
        return directory

    def get_file(self, name: str) -> Optional['File']:
        for file in self._files:
            if file.name == name:
                return file
        return None

    def get_directory(self, name: str) -> Optional['Directory']:
        for directory in self._dirs:
            if directory.name == name:
                return directory
        return None

    def get_size(self) -> int:
        return sum([file.get_size() for file in self._files]) + \
               sum([directory.get_size() for directory in self._dirs])

    def walk(self, fn: Callable[['Directory'], None]):
        """Calls the given function for the current directory and its children
        """
        fn(self)
        for child in self._dirs:
            child.walk(fn)

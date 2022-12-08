class Tree:
    def __init__(self, height: int):
        self._height = height

    def __eq__(self, other: 'Tree'):
        return self._height == other._height

    def __lt__(self, other: 'Tree'):
        return self._height < other._height

    def __le__(self, other: 'Tree'):
        return self._height <= other._height

    def __gt__(self, other: 'Tree'):
        return self._height > other._height

    def __ge__(self, other: 'Tree'):
        return self._height >= other._height

    def __str__(self) -> str:
        return str(self._height)

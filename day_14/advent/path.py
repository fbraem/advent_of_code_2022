from typing import Tuple


class Path:
    def __init__(self):
        self._coordinates = []
        self._current_index = 0

    def add_coordinate(self, coordinate: Tuple[int, int]):
        self._coordinates.append(coordinate)

    def get_min_x(self):
        return min([coordinate[0] for coordinate in self._coordinates])

    def get_max_x(self):
        return max([coordinate[0] for coordinate in self._coordinates])

    def get_min_y(self):
        return min([coordinate[1] for coordinate in self._coordinates])

    def get_max_y(self):
        return max([coordinate[1] for coordinate in self._coordinates])

    def __str__(self) -> str:
        return ' -> '.join([str(coordinate) for coordinate in self._coordinates])

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self._coordinates):
            coordinate = self._coordinates[self._current_index]
            self._current_index += 1
            return coordinate

        raise StopIteration

    def __getitem__(self, item):
        return self._coordinates[item]

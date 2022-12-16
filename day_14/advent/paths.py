from typing import Tuple

from advent.path import Path


class Paths:
    def __init__(self):
        self._paths = set()
        self._sand = set()
        self._current_index = 0

    def copy(self):
        new_paths = Paths()
        new_paths._paths = self._paths.copy()
        return new_paths

    def add_path(self, path: Path):
        for c1, c2 in zip(path, path[1:]):
            if c1[0] == c2[0]:
                if c1[1] <= c2[1]:
                    for y in range(c1[1], c2[1] + 1):
                        self._paths.add((c1[0], y))
                else:
                    for y in range(c2[1], c1[1] + 1):
                        self._paths.add((c1[0], y))
            elif c1[1] == c2[1]:
                if c1[0] <= c2[0]:
                    for x in range(c1[0], c2[0] + 1):
                        self._paths.add((x, c1[1]))
                else:
                    for x in range(c2[0], c1[0] + 1):
                        self._paths.add((x, c1[1]))
            else:
                print(f'Impossible? {c1}, {c2}')

    def block_position(self, pos: Tuple[int, int]):
        self._sand.add(pos)

    def sand(self) -> list[Tuple[int, int]]:
        return list(self._sand)

    def is_rock(self, pos: Tuple[int, int]):
        return pos in self._paths

    def is_sand(self, pos: Tuple[int, int]):
        return pos in self._sand

    def get_min_x(self):
        return min([path[0] for path in self._paths])

    def get_max_y(self):
        return max([path[1] for path in self._paths])

    def get_min_y(self):
        return min([path[1] for path in self._paths])

    def get_max_x(self):
        return max([path[0] for path in self._paths])

    def is_free(self, x: int, y: int):
        return (x, y) not in self._paths and (x, y) not in self._sand

    def __str__(self) -> str:
        return '\n'.join([str(path) for path in self._paths])

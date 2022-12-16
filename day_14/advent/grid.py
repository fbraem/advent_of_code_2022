from typing import Tuple

from advent.paths import Paths


class Grid:
    def __init__(self, paths: Paths, floor: bool = False):
        self._paths = paths
        self._floor = floor

    def drop_sand(self, start_pos: Tuple[int, int]) -> int:
        max_y = self._paths.get_max_y()
        if self._floor:
            max_y += 2

        moves = 0
        x = start_pos[0]
        y = start_pos[1]

        while True:
            if y == max_y:  # We are beneath the last row
                return 0

            if self._paths.is_free(x, y + 1) and y + 1 != max_y:  # down
                y += 1
            elif self._paths.is_free(x - 1, y + 1) and y + 1 != max_y:  # left
                x -= 1
                y += 1
            elif self._paths.is_free(x + 1, y + 1) and y + 1 != max_y:  # right
                x += 1
                y += 1
            elif y == 0:  # on top
                break
            else:  # No more free places, mark position as occupied
                self._paths.block_position((x, y))
                break

            moves += 1

        return moves

    def __str__(self):
        max_y = self._paths.get_max_y() + 1
        if self._floor:
            max_y += 1

        result = ''
        for y in range(0, max_y):
            for x in range(self._paths.get_min_x(), self._paths.get_max_x() + 1):
                if self._paths.is_rock((x, y)):
                    result += '#'
                elif self._paths.is_sand((x, y)):
                    result += 'o'
                else:
                    result += '.'
            result += '\n'

        if self._floor:
            for x in range(self._paths.get_min_x(), self._paths.get_max_x() + 1):
                result += '#'
            result += '\n'

        return result

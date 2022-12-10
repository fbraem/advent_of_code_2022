from typing import Tuple, Optional


def signum(i: int):
    if i > 0:
        return 1
    if i == 0:
        return 0
    if i < 0:
        return -1


class Rope:
    def __init__(self, *knots: Tuple[int, int]):
        self._knots = list(knots)

    @property
    def head(self) -> Tuple[int, int]:
        return self._knots[0]

    @property
    def tail(self) -> Tuple[int, int]:
        return self._knots[-1]

    def move(self, direction: str):
        self.__move_head(direction)
        for index, knot in enumerate(self._knots):
            if index > 0:
                self.__move_knots(direction, index)

    def find_knot(self, pos: Tuple[int, int]) -> int:
        for index, knot in enumerate(self._knots):
            if knot[0] == pos[0] and knot[1] == pos[1]:
                return index
        return -1

    def __move_head(self, direction: str):
        match direction:
            case 'R':  # Right
                self._knots[0] = (self._knots[0][0], self._knots[0][1] + 1)
            case 'L':  # Left
                self._knots[0] = (self._knots[0][0], self._knots[0][1] - 1)
            case 'U':  # Up
                self._knots[0] = (self._knots[0][0] - 1, self._knots[0][1])
            case 'D':  # Down
                self._knots[0] = (self._knots[0][0] + 1, self._knots[0][1])

    def __move_knots(self, direction: str, knot: int):
        # Check if the tail must be moved
        col_distance = self._knots[knot - 1][1] - self._knots[knot][1]
        row_distance = self._knots[knot - 1][0] - self._knots[knot][0]

        if abs(col_distance) > 1 or abs(row_distance) > 1:
            self._knots[knot] = (
                self._knots[knot][0] + signum(row_distance),
                self._knots[knot][1] + signum(col_distance)
            )

    def __str__(self):
        return f'{self._knots[0]=}, {self._knots[1]=}'

from typing import Tuple, Optional


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
        # print(f'{knot=} - {row_distance=} / {col_distance=}')
        if col_distance > 1:
            if row_distance < -1:
                self._knots[knot] = (self._knots[knot-1][0] + 1, self._knots[knot-1][1] - 1)
            else:
                self._knots[knot] = (self._knots[knot - 1][0], self._knots[knot - 1][1] - 1)
        if col_distance < -1:
            self._knots[knot] = (self._knots[knot-1][0], self._knots[knot - 1][1] + 1)

        row_distance = self._knots[knot - 1][0] - self._knots[knot][0]
        # print(f'{knot=} - {row_distance=}')
        if row_distance > 1:
            self._knots[knot] = (self._knots[knot-1][0] - 1, self._knots[knot-1][1])
        if row_distance < -1:
            self._knots[knot] = (self._knots[knot-1][0] + 1, self._knots[knot-1][1])

    def __str__(self):
        return f'{self._knots[0]=}, {self._knots[1]=}'

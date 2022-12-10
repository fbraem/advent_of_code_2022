from typing import Tuple


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
        match direction:
            case 'R':  # Right
                self._knots[0] = (self._knots[0][0], self._knots[0][1] + 1)
            case 'L':  # Left
                self._knots[0] = (self._knots[0][0], self._knots[0][1] - 1)
            case 'U':  # Up
                self._knots[0] = (self._knots[0][0] - 1, self._knots[0][1])
            case 'D':  # Down
                self._knots[0] = (self._knots[0][0] + 1, self._knots[0][1])

        # Check if the tail must be moved
        col_distance = self._knots[-1][1] - self._knots[0][1]
        row_distance = self._knots[-1][0] - self._knots[0][0]
        print(f'{row_distance=}, {col_distance=}')

        if abs(row_distance) > 1 or abs(col_distance) > 1:
            match direction:
                case 'R':
                    self._knots[-1] = (self._knots[0][0], self._knots[0][1] - 1)
                case 'L':
                    self._knots[-1] = (self._knots[0][0], self._knots[0][1] + 1)
                case 'U':
                    self._knots[-1] = (self._knots[0][0] + 1, self._knots[0][1])
                case 'D':
                    self._knots[-1] = (self._knots[0][0] - 1, self._knots[0][1])

    def __str__(self):
        return f'{self._knots[0]=}, {self._knots[1]=}'

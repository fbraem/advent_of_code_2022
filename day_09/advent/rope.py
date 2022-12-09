from typing import Tuple


class Rope:
    def __init__(self, head: Tuple[int, int], tail: Tuple[int, int]):
        self._head = head
        self._tail = tail

    @property
    def head(self) -> Tuple[int, int]:
        return self._head

    @property
    def tail(self) -> Tuple[int, int]:
        return self._tail

    def move(self, direction: str):
        match direction:
            case 'R':  # Right
                self._head = (self._head[0], self._head[1] + 1)
            case 'L':  # Left
                self._head = (self._head[0], self._head[1] - 1)
            case 'U':  # Up
                self._head = (self._head[0] - 1, self._head[1])
            case 'D':  # Down
                self._head = (self._head[0] + 1, self._head[1])

        # Check if the tail must be moved
        col_distance = self._tail[1] - self._head[1]
        row_distance = self._tail[0] - self._head[0]
        print(f'{row_distance=}, {col_distance=}')

        if abs(row_distance) > 1 or abs(col_distance) > 1:
            match direction:
                case 'R':
                    self._tail = (self._head[0], self._head[1] - 1)
                case 'L':
                    self._tail = (self._head[0], self._head[1] + 1)
                case 'U':
                    self._tail = (self._head[0] + 1, self._head[1])
                case 'D':
                    self._tail = (self._head[0] - 1, self._head[1])

    def __str__(self):
        return f'{self._head=}, {self._tail=}'

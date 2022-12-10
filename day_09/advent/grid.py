from typing import Tuple

from advent.rope import Rope


class Grid:
    def __init__(self, rope: Rope):
        self._seen = set()
        self._rope = rope
        self._seen.add(self._rope.head)

    def move_rope(self, direction: str, step: int):
        for i in range(0, step):
            self._rope.move(direction)
            self._seen.add(self._rope.tail)

    def is_visited(self, pos: Tuple[int, int]):
        return len(self._seen.intersection({pos})) > 0

    @property
    def number_of_visits(self) -> int:
        return len(self._seen)

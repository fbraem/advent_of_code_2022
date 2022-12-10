from advent.rope import Rope


class Grid:
    def __init__(self, row: int, col: int, rope: Rope):
        self._grid = []
        for r in range(0, row):
            columns = []
            for c in range(0, col):
                columns.append(0)
            self._grid.append(columns)
        self._rope = rope
        self._grid[self._rope.head[0] - 1][self._rope.head[1] - 1] = 1

    def move_rope(self, direction: str, step: int):
        for i in range(0, step):
            self._rope.move(direction)
            self._grid[self._rope.tail[0] - 1][self._rope.tail[1] - 1] = 1

    def get_visited(self, row: int, col: int) -> int:
        return self._grid[row - 1][col - 1]

    @property
    def number_of_visits(self) -> int:
        count = 0
        for row in self._grid:
            for c in row:
                if c > 0:
                    count += 1
        return count

    def print_visits(self):
        for row in self._grid:
            line = ''
            for c in row:
                if c > 0:
                    line += ' #'
                else:
                    line += ' .'
            print(line)

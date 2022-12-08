from advent.tree import Tree


class Forest:
    def __init__(self):
        self._rows = []

    def add_row(self, *trees: Tree):
        self._rows.append(trees)

    @property
    def row_count(self):
        return len(self._rows)

    def get_tree(self, row: int, col: int):
        return self._rows[row][col]

    def is_tree_visible(self, row: int, col: int) -> bool:
        if row == 0:
            return True
        if row == self.row_count - 1:
            return True
        if col == 0:
            return True
        if col == len(self._rows[row]) - 1:
            return True

        visible_left = all(t < self._rows[row][col] for t in self._rows[row][0:col])
        if visible_left:
            return True

        visible_right = all(t < self._rows[row][col] for t in self._rows[row][col+1:])
        if visible_right:
            return True

        up = []
        for r in range(0, row):
            up.append(self._rows[r][col])
        visible_up = all(t < self._rows[row][col] for t in up)
        if visible_up:
            return True

        down = []
        for r in range(row + 1, self.row_count):
            down.append(self._rows[r][col])
        visible_down = all(t < self._rows[row][col] for t in down)
        if visible_down:
            return True

        return False

    def count_visible_trees(self) -> int:
        count = 0
        for row_index, row in enumerate(self._rows):
            for col_index, tree in enumerate(row):
                if self.is_tree_visible(row_index, col_index):
                    count += 1
        return count

    def get_scenic_score(self, row: int, col: int) -> int:
        left_score = 0
        # from right to left
        for t in self._rows[row][col-1::-1]:
            left_score += 1
            # Stop counting when the tree is taller or has the same height
            if t >= self._rows[row][col]:
                break

        right_score = 0
        # from left to right
        for i, t in enumerate(self._rows[row][col + 1:]):
            right_score += 1
            # Stop counting when the tree is taller or has the same height
            if t >= self._rows[row][col]:
                break

        # First make a list with all trees above
        up = []
        for r in range(row - 1, -1, -1):
            up.append(self._rows[r][col])
        up_score = 0
        for t in up:
            up_score += 1
            # Stop counting when the tree is taller or has the same height
            if t >= self._rows[row][col]:
                break

        # First make a list with all trees down
        down = []
        for r in range(row + 1, self.row_count):
            down.append(self._rows[r][col])
        down_score = 0
        for t in down:
            down_score += 1
            # Stop counting when the tree is taller or has the same height
            if t >= self._rows[row][col]:
                break

        return left_score * right_score * up_score * down_score

    def get_highest_scenic_score(self) -> int:
        max_score = 0
        for row_index, row in enumerate(self._rows):
            for col_index, tree in enumerate(row):
                score = self.get_scenic_score(row_index, col_index)
                if score > max_score:
                    max_score = score
        return max_score

    def __str__(self):
        lines = ''
        for row in self._rows:
            line = ''
            for tree in row:
                line += str(tree)
            lines += line + '\n'
        return lines

    def add_row_from_string(self, tree_string: str):
        # Each char is a number, each number is a tree
        self.add_row(*[Tree(int(number)) for number in tree_string])

from typing import Optional

from advent.stack import Stack


class Stacks:
    def __init__(self):
        self._stacks = []
        self._current_index = 0

    def add(self, *stack: Stack):
        self._stacks.extend(stack)

    @property
    def count(self) -> int:
        return len(self._stacks)

    def find_by_number(self, number: int) -> Optional[Stack]:
        for x in self._stacks:
            if x.number == number:
                return x
        return None

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self.count:
            elf = self._stacks[self._current_index]
            self._current_index += 1
            return elf

        raise StopIteration

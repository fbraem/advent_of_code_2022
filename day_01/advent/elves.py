from typing import Optional

from advent.elf import Elf


class Elves:
    def __init__(self):
        self._elves = []
        self._current_index = 0

    def add(self, *elf: Elf):
        self._elves.extend(elf)

    @property
    def count(self) -> int:
        return len(self._elves)

    def get(self, index: int) -> Optional[Elf]:
        if 0 <= index < self.count:
            return self._elves[index]
        return None

    def get_elf_with_most_calories(self) -> Optional[Elf]:
        if len(self._elves) == 0:
            return None

        elf = self._elves[0]
        for current_elf in self._elves[1:]:
            if current_elf.carried_calories > elf.carried_calories:
                elf = current_elf

        return elf

    def sort(self) -> 'Elves':
        elves = Elves()
        elves._elves = sorted(self._elves, key=lambda x: x.carried_calories, reverse=True)
        return elves

    def clear(self):
        self._elves = []

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self.count:
            elf = self._elves[self._current_index]
            self._current_index += 1
            return elf

        raise StopIteration

from advent.elf import Elf
from advent.elves import Elves
from advent.food import Food


class ElfImporter:
    def __init__(self):
        self._elves = Elves()

    @property
    def elves(self) -> Elves:
        return self._elves

    def read_file(self, path: str):
        self._elves.clear()
        current_elf = None
        with open(path) as file:
            for line in file.readlines():
                if len(line) == 1:
                    current_elf = None
                    continue

                if current_elf is None:
                    current_elf = Elf()
                    self._elves.add(current_elf)

                current_elf.add_food(Food(int(line.rstrip())))

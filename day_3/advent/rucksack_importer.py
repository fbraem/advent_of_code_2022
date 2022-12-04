from advent.group import Group
from advent.rucksack import Rucksack


class RucksackImporter:
    def __init__(self):
        self._rucksacks = []

    @property
    def rucksacks(self):
        return self._rucksacks

    def clear(self):
        self._rucksacks = []

    def read_file(self, path: str):
        self.clear()

        with open(path) as file:
            for line in file.readlines():
                rucksack = Rucksack(line.rstrip())
                self._rucksacks.append(rucksack)

    def get_groups(self) -> list[Group]:
        groups = []

        # Great groups of 3 rucksacks (we assume that the number of rucksacks is a multiple of 3)
        for i in range(0, len(self._rucksacks), 3):
            groups.append(Group(self._rucksacks[i], self._rucksacks[i+1], self._rucksacks[i+2]))

        return groups

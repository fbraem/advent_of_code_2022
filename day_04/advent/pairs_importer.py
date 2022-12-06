from advent.elf import Elf
from advent.pair import Pair


class PairsImporter:
    def __init__(self):
        self._pairs = []

    def clear(self):
        self._pairs = []

    def read_file(self, path: str):
        self.clear()

        with open(path) as file:
            for line in file.readlines():
                stripped = line.rstrip()
                if len(stripped) == 0:
                    continue
                pairs = stripped.split(',')

                elfs = []
                for pair in pairs:
                    sections = pair.split('-')
                    elf = Elf()
                    elf.add_section(int(sections[0]), int(sections[1]))
                    elfs.append(elf)

                self._pairs.append(Pair(elfs[0], elfs[1]))

    @property
    def pairs(self):
        return self._pairs

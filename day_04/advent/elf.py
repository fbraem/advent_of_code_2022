class Elf:
    def __init__(self):
        self._sections = []

    def add_section(self, start: int, end: int):
        for i in range(start, end + 1):
            self._sections.append(i)

    @property
    def sections(self) -> list[int]:
        return self._sections

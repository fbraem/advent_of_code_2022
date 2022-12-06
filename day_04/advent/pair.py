from advent.elf import Elf


class Pair:
    def __init__(self, first: Elf, second: Elf):
        self._pair = first, second

    def is_fully_contained(self) -> bool:
        # Does an elf contain sections which fully contains the other?

        sections_1 = set(self._pair[0].sections)
        sections_2 = set(self._pair[1].sections)

        intersection = sections_1.intersection(sections_2)
        return intersection == sections_1 or intersection == sections_2

    def get_overlaps(self) -> set[int]:
        sections_1 = set(self._pair[0].sections)
        sections_2 = set(self._pair[1].sections)

        return sections_1.intersection(sections_2)

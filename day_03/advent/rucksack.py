from typing import Optional

from advent.item import Item


class Rucksack:
    def __init__(self, items: Optional[str] = None):
        # Two compartments with a list of items
        self._compartments = [], []
        if items:
            self.fill(items)

    @property
    def compartments(self):
        return self._compartments

    @property
    def items(self) -> list[Item]:
        items = []
        for c in self._compartments:
            items.extend(c)
        return items

    def clear(self):
        self._compartments = [], []

    def fill(self, items: str):
        self.clear()

        # Items are distributed equally in the compartments of the rucksack.
        part_length = int(len(items) / len(self._compartments))

        start = 0
        for index, compartment in enumerate(self._compartments):
            part = slice(start, start + part_length)
            for p in list(items)[part]:
                compartment.append(Item(p))
            start += part_length

    def find_shared_item(self) -> Optional[Item]:
        # There is one item that is stored in all compartments, find it

        # First, we look at all the items of the first compartment and see if the item
        # is also available in the other compartments.
        seen = {}
        for item in self._compartments[0]:
            if item.char in seen:
                continue  # No need to count the item multiple times

            seen[item.char] = item, 1
            for compartment in self._compartments[1:]:
                for i in compartment:
                    if i.char == item.char:
                        seen[item.char] = item, seen[item.char][1] + 1
                        break  # Count the item only once

        # Now search in the dictionary for the item that is present in all compartments
        # This is the item with the count == number of compartments.
        # For now, we assume there is only one
        number_of_compartments = len(self._compartments)
        shared_items = [value[0] for char, value in seen.items() if value[1] == number_of_compartments]
        if len(shared_items) > 0:
            return shared_items[0]

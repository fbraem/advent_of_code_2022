from typing import Optional

from advent.item import Item


class Group:
    def __init__(self, *rucksacks):
        self._rucksacks = rucksacks

    def find_badge(self) -> Optional[Item]:
        result = None

        items = {}  # A dictionary with a tuple as value: the item and a list of rucksacks
        for index, rucksack in enumerate(self._rucksacks):
            for item in rucksack.items:
                if item.char in items:
                    if index in items[item.char][1]:
                        # This item was already added for this rucksack, skip it
                        continue
                    items[item.char][1].append(index)
                else:
                    items[item.char] = item, [index]

        number_of_rucksacks = len(self._rucksacks)
        for value in items.values():
            # The item that is present in all rucksacks, is the badge
            if len(value[1]) == number_of_rucksacks:
                result = value[0]
                break

        return result

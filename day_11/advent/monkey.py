from typing import Optional, Tuple

from advent.operation import Operation
from advent.test import Test


class Monkey:
    def __init__(self, number: int):
        self._number = number
        self._operation = None
        self._test = None
        self._items = []
        self._inspections = 0

    @property
    def number(self):
        return self._number

    @property
    def items(self) -> list[int]:
        return self._items

    @property
    def inspections(self) -> int:
        return self._inspections

    @property
    def test(self):
        return self._test

    def add_item(self, *items: int):
        self._items.extend(items)

    def next_item(self) -> Optional[int]:
        if len(self._items) > 0:
            first = self._items[0]
            del self._items[0]
            return first
        return None

    def inspect(self, item: int, change_worry: bool = True) -> Tuple[int, int]:
        # The returned value is a tuple with the number of the new monkey
        # and the new worry level.
        self._inspections += 1
        worry_level = self._operation.execute(item)
        if change_worry:
            worry_level = int(worry_level / 3)
        else:
            worry_level = worry_level
        return self._test.test(worry_level), worry_level

    def set_operation(self, operation: Operation):
        self._operation = operation

    def set_test(self, test: Test):
        self._test = test

    def __str__(self):
        return f'Monkey {self._number}: {self._items} - inspected: {self._inspections}'

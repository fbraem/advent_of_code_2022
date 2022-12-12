from typing import Optional

from advent.monkey import Monkey


class Monkeys:
    def __init__(self):
        self._monkeys = []
        self._current_index = 0

    def add(self, monkey: Monkey):
        self._monkeys.append(monkey)

    def find(self, number: int) -> Optional[Monkey]:
        return next(
            (monkey for monkey in self._monkeys if monkey.number == number),
            None
        )

    def play_round(self, change_worry: bool = True):
        modulo = 1
        for monkey in self._monkeys:
            modulo *= monkey.test.divisible_by

        for monkey in self._monkeys:
            while True:
                item = monkey.next_item()
                if item is None:
                    break
                new_monkey_number, worry_level = monkey.inspect(item, change_worry)
                new_monkey = self.find(new_monkey_number)
                if new_monkey is None:
                    print(f'Could not find monkey {new_monkey_number}')
                    break
                if change_worry:
                    new_monkey.add_item(worry_level)
                else:
                    new_monkey.add_item(worry_level % modulo)

    @property
    def monkey_business(self):
        all_inspections = sorted([monkey.inspections for monkey in self._monkeys], reverse=True)
        return all_inspections[0] * all_inspections[1]

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self._monkeys):
            monkey = self._monkeys[self._current_index]
            self._current_index += 1
            return monkey

        raise StopIteration

    def __str__(self) -> str:
        result = ''

        for monkey in self:
            result += str(monkey) + '\n'

        return result

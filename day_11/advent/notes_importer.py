import re

from advent.monkey import Monkey
from advent.monkeys import Monkeys
from advent.operation import Operation
from advent.test import Test


class NotesImporter:
    def __init__(self):
        self._monkeys = Monkeys()

    @property
    def monkeys(self):
        return self._monkeys

    def read_file(self, path: str):
        self._monkeys = Monkeys()
        monkey = None

        # Note: no time to write a real parsing state machine :)
        with open(path) as file:
            while True:
                line = file.readline()
                if not line:
                    break

                stripped_line = line.rstrip()
                match = re.match(r'Monkey (\d):', stripped_line)
                if match:
                    monkey = Monkey(int(match.groups()[0]))
                    self._monkeys.add(monkey)
                    continue

                if stripped_line.startswith('  Starting items:'):
                    _, numbers = stripped_line.split(':')
                    monkey.add_item(*[int(number) for number in numbers.split(', ')])

                if stripped_line.startswith('  Operation:'):
                    _, operation = stripped_line.split(':')
                    match = re.match(r'(.*)\s*=\s*(.*)\s*([+\-*\/])\s*(.*)', operation)
                    if match:
                        monkey.set_operation(Operation(match.groups()[1], match.groups()[2], match.groups()[3]))

                if stripped_line.startswith('  Test: '):
                    _, test = stripped_line.split(':')
                    number = re.findall(r'\d+', test)
                    if len(number) > 0:
                        divisible_by = int(number[0])
                        # Read the next line for true
                        true_line = file.readline()
                        if not true_line:
                            break
                        number = re.findall(r'\d+', true_line)
                        if len(number) > 0:
                            when_true = int(number[0])

                        # Read the next line for false
                        false_line = file.readline()
                        if not false_line:
                            break
                        number = re.findall(r'\d+', false_line)
                        if len(number) > 0:
                            when_false = int(number[0])

                        monkey.set_test(Test(divisible_by, when_true, when_false))

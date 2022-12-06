import re
from enum import Enum

from advent.action import Action
from advent.plan import Plan
from advent.stack import Stack


class StateEnum(Enum):
    READING_STACK = 0
    READING_ACTION = 1


class PlanImporter:
    def __init__(self):
        self._plan = Plan()

    @property
    def plan(self):
        return self._plan

    def read_file(self, path: str):
        stack_lines = []
        action_lines = []

        state = StateEnum.READING_STACK
        with open(path) as file:
            # First read stack information
            for line in file:
                stripped_line = line.rstrip()
                if len(stripped_line) == 0:
                    state = StateEnum.READING_ACTION
                    continue

                if state == StateEnum.READING_STACK:
                    stack_lines.append(stripped_line)
                else:
                    action_lines.append(stripped_line)

        self.__process_stacks(stack_lines)
        self.__process_actions(action_lines)

    def __process_stacks(self, stack_lines: list[str]):
        stack_line = stack_lines.pop()
        for stack_number in stack_line.rsplit():
            self._plan.add_stack(Stack(int(stack_number)))

        for crate_line in reversed(stack_lines):
            for match in re.finditer(r"\[(.)\]", crate_line):
                # Determine the stack number based on the start of the match
                stack_number = int(match.start() / 4 + 1)
                self._plan.add_crate_to_stack(stack_number, match.group()[1])

    def __process_actions(self, action_lines: list[str]):
        self._actions = []
        for line in action_lines:
            m = re.search(r"move (\d+) from (\d+) to (\d+)", line)
            self.plan.add_action(
                Action(
                    int(m.group(1)),
                    int(m.group(2)),
                    int(m.group(3)),
                )
            )

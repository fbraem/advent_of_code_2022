from typing import Optional

from advent.action import Action
from advent.stack import Stack
from advent.stacks import Stacks


class Plan:
    def __init__(self):
        self._stacks = Stacks()
        self._actions = []

    def add_stack(self, *stack: Stack):
        self._stacks.add(*stack)

    def add_crate_to_stack(self, stack_number: int, crate: str):
        stack = self._stacks.find_by_number(stack_number)
        if stack:
            stack.add_crate(crate)

    def add_action(self, *action: Action):
        self._actions.extend(action)

    @property
    def stacks(self):
        return self._stacks

    @property
    def action_count(self):
        return len(self._actions)

    @property
    def actions(self) -> list[Action]:
        return self._actions

    def execute(self):
        for action in self._actions:
            action.execute(self._stacks)

    def execute_contain_order(self):
        for action in self._actions:
            action.execute_contain_order(self._stacks)

    def get_top_crates(self) -> str:
        result = ''
        for stack in self._stacks:
            result += stack.top_crate
        return result

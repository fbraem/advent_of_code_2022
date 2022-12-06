import unittest

from advent.action import Action
from advent.stack import Stack
from advent.stacks import Stacks


class ActionTest(unittest.TestCase):
    def test_execute(self):
        stack_1 = Stack(1)
        stack_1.add_crate('Z', 'N')
        stack_2 = Stack(2)
        stack_2.add_crate('M', 'C', 'D')
        stack_3 = Stack(3)
        stack_3.add_crate('P')
        stacks = Stacks()
        stacks.add(stack_1, stack_2, stack_3)

        action = Action(1, 2, 1)
        action.execute(stacks)

        self.assertEqual(stack_1.crates, ['Z', 'N', 'D'], 'Stack 1 should contain Z, N, D')
        self.assertEqual(stack_2.crates, ['M', 'C'], 'Stack 2 should contain M, C')
        self.assertEqual(stack_3.crates, ['P'], 'Stack 3 should contain P')

        action = Action(3, 1, 3)
        action.execute(stacks)
        self.assertEqual(stack_1.crates, [], 'Stack 1 should be empty')
        self.assertEqual(stack_2.crates, ['M', 'C'], 'Stack 2 should contain M, C')
        self.assertEqual(stack_3.crates, ['P', 'D', 'N', 'Z'], 'Stack 3 should contain P, D, N, Z')

        self.assertEqual(stack_2.top_crate, 'C', 'The top should be C')
        self.assertEqual(stack_3.top_crate, 'Z', 'The top should be Z')

    def test_execute_contain_order(self):
        stack_1 = Stack(1)
        stack_1.add_crate('Z', 'N')
        stack_2 = Stack(2)
        stack_2.add_crate('M', 'C', 'D')
        stack_3 = Stack(3)
        stack_3.add_crate('P')
        stacks = Stacks()
        stacks.add(stack_1, stack_2, stack_3)

        action = Action(1, 2, 1)
        action.execute_contain_order(stacks)

        self.assertEqual(stack_1.crates, ['Z', 'N', 'D'], 'Stack 1 should contain Z, N, D')
        self.assertEqual(stack_2.crates, ['M', 'C'], 'Stack 2 should contain M, C')
        self.assertEqual(stack_3.crates, ['P'], 'Stack 3 should contain P')

        action = Action(3, 1, 3)
        action.execute_contain_order(stacks)
        self.assertEqual(stack_1.crates, [], 'Stack 1 should be empty')
        self.assertEqual(stack_2.crates, ['M', 'C'], 'Stack 2 should contain M, C')
        self.assertEqual(stack_3.crates, ['P', 'Z', 'N', 'D'], 'Stack 3 should contain P, Z, N, D')

        self.assertEqual(stack_2.top_crate, 'C', 'The top should be C')
        self.assertEqual(stack_3.top_crate, 'D', 'The top should be D')

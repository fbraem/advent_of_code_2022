import unittest

from advent.action import Action
from advent.plan import Plan
from advent.stack import Stack


class PlanTests(unittest.TestCase):
    def test_execute(self):
        plan = Plan()

        stack_1 = Stack(1)
        stack_1.add_crate('Z', 'N')
        stack_2 = Stack(2)
        stack_2.add_crate('M', 'C', 'D')
        stack_3 = Stack(3)
        stack_3.add_crate('P')
        plan.add_stack(stack_1, stack_2, stack_3)

        self.assertEqual(plan.stacks.count, 3, 'There should be 3 stacks')

        plan.add_action(
            Action(1, 2, 1),
            Action(3, 1, 3),
            Action(2, 2, 1),
            Action(1, 1, 2)
        )
        plan.execute()

        self.assertEqual(plan.get_top_crates(), 'CMZ', 'Top should be CMZ')

    def test_execute_contain_order(self):
        plan = Plan()

        stack_1 = Stack(1)
        stack_1.add_crate('Z', 'N')
        stack_2 = Stack(2)
        stack_2.add_crate('M', 'C', 'D')
        stack_3 = Stack(3)
        stack_3.add_crate('P')
        plan.add_stack(stack_1, stack_2, stack_3)

        self.assertEqual(plan.stacks.count, 3, 'There should be 3 stacks')

        plan.add_action(
            Action(1, 2, 1),
            Action(3, 1, 3),
            Action(2, 2, 1),
            Action(1, 1, 2)
        )
        plan.execute_contain_order()

        self.assertEqual(plan.get_top_crates(), 'MCD', 'Top should be MCD')

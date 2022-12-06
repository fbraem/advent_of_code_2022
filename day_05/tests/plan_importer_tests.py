import unittest
from textwrap import dedent
from unittest import mock

from advent.plan_importer import PlanImporter

TEST_DATA = dedent("""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""")


class PlanImporterTests(unittest.TestCase):
    @mock.patch("builtins.open", mock.mock_open(read_data=TEST_DATA))
    def test_import(self):
        importer = PlanImporter()
        importer.read_file('test')

        self.assertEqual(importer.plan.stacks.count, 3, 'There should be 3 stacks')
        self.assertIsNotNone(importer.plan.stacks.find_by_number(1), 'There should be a stack with number 1')

        stack = importer.plan.stacks.find_by_number(1)
        self.assertEqual(stack.crates, ['Z', 'N'], 'The first stack should contain Z and N')
        stack = importer.plan.stacks.find_by_number(2)
        self.assertEqual(stack.crates, ['M', 'C', 'D'], 'The second stack should contain M, C and D')
        stack = importer.plan.stacks.find_by_number(3)
        self.assertEqual(stack.crates, ['P'], 'The third stack should contain P')

        self.assertEqual(importer.plan.action_count, 4, 'There should be 4 actions')
        self.assertEqual(importer.plan.actions[0].count, 1, 'The stack number should be 1')
        self.assertEqual(importer.plan.actions[0].current, 2, 'Current stack number should be 2')
        self.assertEqual(importer.plan.actions[0].to, 1, 'The new stack number should be 1')

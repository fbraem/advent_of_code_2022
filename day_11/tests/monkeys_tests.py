import unittest

from advent.monkey import Monkey
from advent.monkeys import Monkeys
from advent.operation import Operation
from advent.test import Test


class MonkeysTests(unittest.TestCase):
    def test_find(self):
        monkeys = Monkeys()
        monkeys.add(Monkey(1))
        monkeys.add(Monkey(2))
        monkeys.add(Monkey(3))

        monkey = monkeys.find(2)
        self.assertIsNotNone(monkey, 'There should be a monkey with number 2')
        self.assertIsNone(monkeys.find(4), 'There is no monkey with number 4')

    def test_sample(self):
        monkeys = Monkeys()
        monkey_0 = Monkey(0)
        monkey_0.add_item(79, 98)
        monkey_0.set_operation(Operation('old', '*', '19'))
        monkey_0.set_test(Test(23, 2, 3))
        monkeys.add(monkey_0)

        monkey_1 = Monkey(1)
        monkey_1.add_item(54, 65, 75, 74)
        monkey_1.set_operation(Operation('old', '+', '6'))
        monkey_1.set_test(Test(19, 2, 0))
        monkeys.add(monkey_1)

        monkey_2 = Monkey(2)
        monkey_2.add_item(79, 60, 97)
        monkey_2.set_operation(Operation('old', '*', 'old'))
        monkey_2.set_test(Test(13, 1, 3))
        monkeys.add(monkey_2)

        monkey_3 = Monkey(3)
        monkey_3.add_item(74)
        monkey_3.set_operation(Operation('old', '+', '3'))
        monkey_3.set_test(Test(17, 0, 1))
        monkeys.add(monkey_3)

        # monkeys.play_round()
        # self.assertEqual([20, 23, 27, 26], monkey_0.items)
        # self.assertEqual([2080, 25, 167, 207, 401, 1046], monkey_1.items)
        # self.assertEqual([], monkey_2.items, 'Monkey 2 should have no items')
        # self.assertEqual([], monkey_3.items, 'Monkey 3 should have no items')

        for i in range(0, 10000):
            print(i)
            monkeys.play_round(change_worry=False)

        print(monkeys)

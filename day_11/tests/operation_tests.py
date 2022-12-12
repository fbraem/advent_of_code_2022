import unittest

from advent.operation import Operation


class OperationTests(unittest.TestCase):
    def test_execute_addition(self):
        op = Operation('old', '+', '7')
        self.assertEqual(20, op.execute(13), 'Operation should result in 20')

    def test_execute_multiply(self):
        op = Operation('old', '*', '7')
        self.assertEqual(14, op.execute(2), 'Operation should result in 14')

    def test_execute_addition_with_old(self):
        op = Operation('old', '+', 'old')
        self.assertEqual(6, op.execute(3), 'Operation should result in 6')

    def test_execute_multiply_with_old(self):
        op = Operation('old', '*', 'old')
        self.assertEqual(9, op.execute(3), 'Operation should result in 9')

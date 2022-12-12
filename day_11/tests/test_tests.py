import unittest

from advent.test import Test


class TestTests(unittest.TestCase):
    def test_test(self):
        test = Test(19, 6, 7)

        self.assertEqual(6, test.test(38), 'Number 6 should be returned')
        self.assertEqual(7, test.test(20), 'Number 7 should be returned')

import unittest

from advent.rope import Rope


class RopeTests(unittest.TestCase):
    def test_right(self):
        rope = Rope((5, 1), (5, 1))
        rope.move('R')
        self.assertEqual((5, 2), rope.head, 'The head of the rope should be on 5, 2')
        self.assertEqual((5, 1), rope.tail, 'The tail of the rope should be on 5, 1')
        rope.move('R')
        self.assertEqual((5, 3), rope.head, 'The head of the rope should be on 5, 3')
        self.assertEqual((5, 2), rope.tail, 'The tail of the rope should be on 5, 2')
        rope.move('R')
        self.assertEqual((5, 4), rope.head, 'The head of the rope should be on 5, 4')
        self.assertEqual((5, 3), rope.tail, 'The tail of the rope should be on 5, 3')
        rope.move('R')
        self.assertEqual((5, 5), rope.head, 'The head of the rope should be on 5, 5')
        self.assertEqual((5, 4), rope.tail, 'The tail of the rope should be on 5, 4')

    def test_up(self):
        rope = Rope((5, 5), (5, 4))
        rope.move('U')
        self.assertEqual((4, 5), rope.head, 'The head of the rope should be on 4, 5')
        self.assertEqual((5, 4), rope.tail, 'The tail of the rope should be on 5, 4')
        rope.move('U')
        self.assertEqual((3, 5), rope.head, 'The head of the rope should be on 3, 5')
        self.assertEqual((4, 5), rope.tail, 'The tail of the rope should be on 4, 5')
        rope.move('U')
        self.assertEqual((2, 5), rope.head, 'The head of the rope should be on 2, 5')
        self.assertEqual((3, 5), rope.tail, 'The tail of the rope should be on 3, 5')
        rope.move('U')
        self.assertEqual((1, 5), rope.head, 'The head of the rope should be on 1, 5')
        self.assertEqual((2, 5), rope.tail, 'The tail of the rope should be on 2, 5')

    def test_left(self):
        rope = Rope((1, 5), (2, 5))
        rope.move('L')
        rope.move('L')
        rope.move('L')
        self.assertEqual((1, 2), rope.head, 'The head of the rope should be on 1, 2')
        self.assertEqual((1, 3), rope.tail, 'The tail of the rope should be on 1, 3')

    def test_down(self):
        rope = Rope((1, 2), (1, 3))
        rope.move('D')
        self.assertEqual((2, 2), rope.head, 'The head of the rope should be on 1, 2')
        self.assertEqual((1, 3), rope.tail, 'The tail of the rope should be on 1, 3')

    def test_right_2(self):
        rope = Rope((2, 2), (1, 3))
        rope.move('R')
        rope.move('R')
        rope.move('R')
        rope.move('R')
        self.assertEqual((2, 6), rope.head, 'The head of the rope should be on 2, 6')
        self.assertEqual((2, 5), rope.tail, 'The tail of the rope should be on 2, 5')

    def test_down_2(self):
        rope = Rope((2, 6), (2, 5))
        rope.move('D')
        self.assertEqual((3, 6), rope.head, 'The head of the rope should be on 3, 6')
        self.assertEqual((2, 5), rope.tail, 'The tail of the rope should be on 2, 5')

    def test_left_2(self):
        rope = Rope((3, 6), (2, 5))
        rope.move('L')
        self.assertEqual((3, 5), rope.head, 'The head of the rope should be on 3, 5')
        self.assertEqual((2, 5), rope.tail, 'The tail of the rope should be on 2, 5')
        rope.move('L')
        self.assertEqual((3, 4), rope.head, 'The head of the rope should be on 3, 4')
        self.assertEqual((2, 5), rope.tail, 'The tail of the rope should be on 2, 5')
        rope.move('L')
        self.assertEqual((3, 3), rope.head, 'The head of the rope should be on 3, 3')
        self.assertEqual((3, 4), rope.tail, 'The tail of the rope should be on 3, 4')
        rope.move('L')
        self.assertEqual((3, 2), rope.head, 'The head of the rope should be on 3, 2')
        self.assertEqual((3, 3), rope.tail, 'The tail of the rope should be on 3, 3')
        rope.move('L')
        self.assertEqual((3, 1), rope.head, 'The head of the rope should be on 3, 1')
        self.assertEqual((3, 2), rope.tail, 'The tail of the rope should be on 3, 2')

    def test_right_3(self):
        rope = Rope((3, 1), (3, 2))
        rope.move('R')
        rope.move('R')
        self.assertEqual((3, 3), rope.head, 'The head of the rope should be on 3, 3')
        self.assertEqual((3, 2), rope.tail, 'The tail of the rope should be on 3, 2')

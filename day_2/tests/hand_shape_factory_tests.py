import unittest

from advent.hand_shape import HandShapeFactory, Rock, Paper, Scissors


class HandShapeFactoryTests(unittest.TestCase):
    def test_create_rock(self):
        hand_shape = HandShapeFactory().create_hand_shape('A')
        self.assertIsInstance(hand_shape, Rock)
        hand_shape = HandShapeFactory().create_hand_shape('X')
        self.assertIsInstance(hand_shape, Rock)

    def test_create_paper(self):
        hand_shape = HandShapeFactory().create_hand_shape('B')
        self.assertIsInstance(hand_shape, Paper)
        hand_shape = HandShapeFactory().create_hand_shape('Y')
        self.assertIsInstance(hand_shape, Paper)

    def test_create_scissors(self):
        hand_shape = HandShapeFactory().create_hand_shape('C')
        self.assertIsInstance(hand_shape, Scissors)
        hand_shape = HandShapeFactory().create_hand_shape('Z')
        self.assertIsInstance(hand_shape, Scissors)

    def test_winning(self):
        scissors = HandShapeFactory().create_hand_shape('C')
        winning_shape = HandShapeFactory.create_winning_shape(scissors.code)
        self.assertEqual(winning_shape.code, 'A')

        paper = HandShapeFactory().create_hand_shape('B')
        winning_shape = HandShapeFactory.create_winning_shape(paper.code)
        self.assertEqual(winning_shape.code, 'C')

        rock = HandShapeFactory().create_hand_shape('A')
        winning_shape = HandShapeFactory.create_winning_shape(rock.code)
        self.assertEqual(winning_shape.code, 'B')

    def test_loosing(self):
        scissors = HandShapeFactory().create_hand_shape('C')
        loosing_shape = HandShapeFactory.create_loosing_shape(scissors.code)
        self.assertEqual(loosing_shape.code, 'B')

        paper = HandShapeFactory().create_hand_shape('B')
        loosing_shape = HandShapeFactory.create_loosing_shape(paper.code)
        self.assertEqual(loosing_shape.code, 'A')

        rock = HandShapeFactory().create_hand_shape('A')
        loosing_shape = HandShapeFactory.create_loosing_shape(rock.code)
        self.assertEqual(loosing_shape.code, 'C')

import unittest

from advent.hand_shape import Rock, Paper, Scissors, Result


class HandShapeTests(unittest.TestCase):
    def test_rock(self):
        rock = Rock()
        paper = Paper()
        scissors = Scissors()

        self.assertEqual(
            rock.play(paper),
            (Result.LOSS.value + rock.score, Result.WIN.value + paper.score)
        )
        self.assertEqual(
            rock.play(scissors),
            (Result.WIN.value + rock.score, Result.LOSS.value + scissors.score)
        )
        self.assertEqual(
            rock.play(rock),
            (Result.DRAW.value + rock.score, Result.DRAW.value + rock.score)
        )

    def test_paper(self):
        rock = Rock()
        paper = Paper()
        scissors = Scissors()

        self.assertEqual(
            paper.play(paper),
            (Result.DRAW.value + paper.score, Result.DRAW.value + paper.score)
        )
        self.assertEqual(
            paper.play(scissors),
            (Result.LOSS.value + paper.score, Result.WIN.value + scissors.score)
        )
        self.assertEqual(
            paper.play(rock),
            (Result.WIN.value + paper.score, Result.LOSS.value + rock.score)
        )

    def test_scissors(self):
        rock = Rock()
        paper = Paper()
        scissors = Scissors()

        self.assertEqual(
            scissors.play(paper),
            (Result.WIN.value + scissors.score, Result.LOSS.value + paper.score)
        )
        self.assertEqual(
            scissors.play(scissors),
            (Result.DRAW.value + scissors.score, Result.DRAW.value + scissors.score)
        )
        self.assertEqual(
            scissors.play(rock),
            (Result.LOSS.value + scissors.score, Result.WIN.value + rock.score)
        )

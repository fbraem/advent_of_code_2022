import unittest

from advent.strategy_guide import StrategyGuide


class StrategyGuideTest(unittest.TestCase):
    def test_play(self):
        strategy_guide = StrategyGuide()
        strategy_guide.add_strategy(
            ('A', 'Y'),
            ('B', 'X'),
            ('C', 'Z')
        )
        result = strategy_guide.play()
        self.assertEqual(result[0], 15)

    def test_play_2(self):
        strategy_guide = StrategyGuide()
        strategy_guide.add_strategy(
            ('A', 'Y'),
            ('B', 'X'),
            ('C', 'Z')
        )
        result = strategy_guide.play_part_2()
        print(result)
        self.assertEqual(result[0], 12)

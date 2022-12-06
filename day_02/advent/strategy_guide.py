from enum import Enum
from typing import Tuple

from advent.hand_shape import HandShapeFactory


class GameResult(Enum):
    LOOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'


class StrategyGuide:
    def __init__(self):
        self._strategies = []

    def clear(self):
        self._strategies.clear()

    def add_strategy(self, *strategy: Tuple[str, str]):
        self._strategies.extend(strategy)

    def play(self) -> Tuple[int, int]:
        result = [0, 0]
        shape_factory = HandShapeFactory()

        for strategy in self._strategies:
            opponent_shape = shape_factory.create_hand_shape(strategy[0])
            my_shape = shape_factory.create_hand_shape(strategy[1])

            play_result = my_shape.play(opponent_shape)
            result[0] += play_result[0]
            result[1] += play_result[1]

        return result[0], result[1]

    def play_part_2(self):
        result = [0, 0]
        shape_factory = HandShapeFactory()

        for strategy in self._strategies:
            opponent_shape = shape_factory.create_hand_shape(strategy[0])
            match strategy[1]:
                case GameResult.DRAW.value:
                    my_shape = shape_factory.create_hand_shape(opponent_shape.code)
                case GameResult.LOOSE.value:
                    my_shape = HandShapeFactory.create_loosing_shape(opponent_shape.code)
                case GameResult.WIN.value:
                    my_shape = HandShapeFactory.create_winning_shape(opponent_shape.code)
                case _:
                    print(f'Unknown game result {strategy[1]} found')
                    continue

            play_result = my_shape.play(opponent_shape)
            result[0] += play_result[0]
            result[1] += play_result[1]

        return result[0], result[1]

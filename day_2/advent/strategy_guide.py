from typing import Tuple

from advent.hand_shape import HandShapeFactory


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
            if strategy[1] == 'Y':  # DRAW
                my_shape = shape_factory.create_hand_shape(opponent_shape.code)
            elif strategy[1] == 'X':  # LOOSE
                my_shape = HandShapeFactory.create_loosing_shape(opponent_shape.code)
            else:  # WIN
                my_shape = HandShapeFactory.create_winning_shape(opponent_shape.code)

            print(opponent_shape.code, my_shape.code)

            play_result = my_shape.play(opponent_shape)
            print(play_result)
            result[0] += play_result[0]
            result[1] += play_result[1]

        return result[0], result[1]

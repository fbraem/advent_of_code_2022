from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Tuple


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


class HandShape(ABC):
    def __init__(self, code: str, score: int):
        self._code = code
        self._score = score

    @property
    def code(self) -> str:
        return self._code

    @property
    def score(self) -> int:
        return self._score

    def play(self, challenger: 'HandShape') -> Tuple[int, int]:
        result = self._do_play(challenger)
        return result[0].value + self.score, result[1].value + challenger.score

    @abstractmethod
    def _do_play(self, challenger: 'HandShape') -> tuple[Result]:
        pass


class Rock(HandShape):
    Code = 'A'

    def __init__(self, code: Optional[str] = Code):
        super().__init__(code, 1)

    def _do_play(self, challenger: 'HandShape') -> Tuple[Result, Result]:
        if isinstance(challenger, Paper):
            return Result.LOSS, Result.WIN
        if isinstance(challenger, Scissors):
            return Result.WIN, Result.LOSS
        return Result.DRAW, Result.DRAW


class Paper(HandShape):
    Code = 'B'

    def __init__(self, code: Optional[str] = Code):
        super().__init__(code, 2)

    def _do_play(self, challenger: 'HandShape') -> Tuple[Result, Result]:
        if isinstance(challenger, Scissors):
            return Result.LOSS, Result.WIN
        if isinstance(challenger, Rock):
            return Result.WIN, Result.LOSS

        return Result.DRAW, Result.DRAW


class Scissors(HandShape):
    Code = 'C'

    def __init__(self, code: Optional[str] = Code):
        super().__init__(code, 3)

    def _do_play(self, challenger: 'HandShape') -> Tuple[Result, Result]:
        if isinstance(challenger, Rock):
            return Result.LOSS, Result.WIN
        if isinstance(challenger, Paper):
            return Result.WIN, Result.LOSS

        return Result.DRAW, Result.DRAW


class HandShapeFactory:
    def __init__(self):
        self._shapes = {
            Rock.Code: Rock,
            'X': Rock,
            Paper.Code: Paper,
            'Y': Paper,
            Scissors.Code: Scissors,
            'Z': Scissors
        }

    def create_hand_shape(self, code: str) -> Optional[HandShape]:
        if code in self._shapes:
            return self._shapes[code](code)

        return None

    @classmethod
    def create_loosing_shape(cls, code: str) -> HandShape:
        if code == Rock.Code:
            return Scissors()
        elif code == Paper.Code:
            return Rock()
        elif code == Scissors.Code:
            return Paper()

    @classmethod
    def create_winning_shape(cls, code: str) -> HandShape:
        if code == Rock.Code:
            return Paper()
        elif code == Paper.Code:
            return Scissors()
        elif code == Scissors.Code:
            return Rock()

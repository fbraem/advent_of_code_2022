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
    Score = 1

    def __init__(self, code: Optional[str] = Code):
        super().__init__(code, Rock.Score)

    def _do_play(self, challenger: 'HandShape') -> Tuple[Result, Result]:
        if isinstance(challenger, Paper):
            return Result.LOSS, Result.WIN
        if isinstance(challenger, Scissors):
            return Result.WIN, Result.LOSS
        return Result.DRAW, Result.DRAW


class Paper(HandShape):
    Code = 'B'
    Score = 2

    def __init__(self, code: Optional[str] = Code):
        super().__init__(code, Paper.Score)

    def _do_play(self, challenger: 'HandShape') -> Tuple[Result, Result]:
        if isinstance(challenger, Scissors):
            return Result.LOSS, Result.WIN
        if isinstance(challenger, Rock):
            return Result.WIN, Result.LOSS

        return Result.DRAW, Result.DRAW


class Scissors(HandShape):
    Code = 'C'
    Score = 3

    def __init__(self, code: Optional[str] = Code):
        super().__init__(code, Scissors.Score)

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
        match code:
            case Rock.Code:
                return Scissors()
            case Paper.Code:
                return Rock()
            case Scissors.Code:
                return Paper()

    @classmethod
    def create_winning_shape(cls, code: str) -> HandShape:
        match code:
            case Rock.Code:
                return Paper()
            case Paper.Code:
                return Scissors()
            case Scissors.Code:
                return Rock()

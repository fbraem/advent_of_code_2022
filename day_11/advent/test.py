class Test:
    def __init__(self, divisible_by: int, when_true: int, when_false: int):
        self._divisible_by = divisible_by
        self._when_true = when_true
        self._when_false = when_false

    @property
    def divisible_by(self) -> int:
        return self._divisible_by

    def test(self, value: int) -> int:
        return self._when_true if value % self._divisible_by == 0 else self._when_false

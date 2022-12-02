class Food:
    def __init__(self, calories: int):
        self._calories = calories

    @property
    def calories(self) -> int:
        return self._calories

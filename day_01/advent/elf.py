from advent.food import Food


class Elf:
    def __init__(self):
        self._foods = []

    def add_food(self, *food: Food):
        self._foods.extend(list(food))

    @property
    def load_count(self):
        return len(self._foods)

    @property
    def carried_calories(self):
        result = 0
        for food in self._foods:
            result += food.calories

        return result

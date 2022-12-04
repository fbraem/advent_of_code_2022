from advent.priorities import Priorities

priorities = Priorities()


class Item:
    def __init__(self, char: str):
        self._char = char
        self._priority = priorities.get(char)

    @property
    def char(self):
        return self._char

    @property
    def priority(self):
        return self._priority

    def __repr__(self):
        return self._char

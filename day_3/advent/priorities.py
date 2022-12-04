class Priorities:
    def __init__(self):
        self._priorities = {}
        for i in range(ord('a'), ord('z') + 1):
            self._priorities[chr(i)] = i - ord('a') + 1
        for i in range(ord('A'), ord('Z') + 1):
            self._priorities[chr(i)] = i - ord('A') + 27

    def get(self, char: str):
        return self._priorities[char]

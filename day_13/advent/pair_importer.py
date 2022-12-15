from functools import cmp_to_key


class PairImporter:
    def __init__(self):
        self._data = []

    @property
    def data(self):
        return self._data

    def read_file(self, path: str):
        with open(path) as file:
            for line in file:
                stripped_line = line.rstrip()
                if len(stripped_line) == 0:
                    continue
                self._data.append(eval(stripped_line))

    def compare(self):
        result = 0
        for i in range(0, len(self._data), 2):
            if self.__compare(self._data[i], self._data[i+1]) == -1:
                result += i
        return result

    def __compare(self, left, right):
        if type(left) is int:
            if type(right) is int:
                return 0 if left == right else 1 if left > right else -1
            return self.__compare([left], right)

        if type(right) is int:
            return self.__compare(left, [right])

        if type(left) is list and type(right) is list:
            for l_value, r_value in zip(left, right):
                result = self.__compare(l_value, r_value)
                if result != 0:
                    return result
            return self.__compare(len(left), len(right))

    def sort(self):
        self._data.append([[2]])
        self._data.append([[6]])
        self._data.sort(key=cmp_to_key(self.__compare))
        return (
            1 + self._data.index([[2]]),
            1 + self._data.index([[6]])
        )

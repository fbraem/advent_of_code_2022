class Operation:
    def __init__(self, arg_1: str, operand: str, arg_2: str):
        self._arg_1 = arg_1
        self._operand = operand
        self._arg_2 = arg_2

    def execute(self, old: int) -> int:
        arg_2 = old if self._arg_2 == 'old' else int(self._arg_2)

        match self._operand:
            case '*':
                return old * arg_2
            case '+':
                return old + arg_2
            case _:
                return old

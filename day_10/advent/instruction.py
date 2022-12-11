from abc import ABC, abstractmethod


class Instruction(ABC):
    def __init__(self, action: str):
        self._action = action

    @abstractmethod
    def execute(self, cpu: 'CPU'):
        pass


class Noop(Instruction):
    name = 'noop'

    def __init__(self):
        super().__init__(Noop.name)

    def execute(self, cpu: 'CPU'):
        cpu.add_cycle()


class AddX(Instruction):
    name = 'addx'

    def __init__(self, value: int):
        super().__init__(AddX.name)
        self._value = value

    def execute(self, cpu: 'CPU'):
        cpu.add_cycle()
        cpu.add_cycle()
        cpu.update_register(self._value)


class InstructionFactory:
    @classmethod
    def create_instruction(cls, *args) -> Instruction:
        if args[0] == Noop.name:
            return Noop()
        return AddX(int(args[1]))

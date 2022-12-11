from advent.instruction import Instruction


class CPU:
    def __init__(self):
        self._cycles = 0
        self._register = 1
        self._signals = [20, 60, 100, 140, 180, 220]
        self._signal_strengths = []
        self._crt = ''
        self._sprite_pos = [0, 1, 2]

    @property
    def register(self) -> int:
        return self._register

    @property
    def crt(self):
        crt = []
        for index in range(0, len(self._crt), 40):
            crt.append(self._crt[index:index + 40])
        return crt

    @property
    def cycles(self) -> int:
        return self._cycles

    @property
    def signal_strengths(self) -> list[int]:
        return self._signal_strengths

    def update_register(self, value: int):
        self._register += value
        self._sprite_pos = [self._register - 1, self._register, self._register + 1]

    def add_cycle(self):
        self._cycles += 1
        if len(self._crt) % 40 in self._sprite_pos:
            self._crt += '#'
        else:
            self._crt += '.'

        if self._cycles in self._signals:
            self._signal_strengths.append(self.cycles * self._register)

    def execute(self, instruction: Instruction):
        instruction.execute(self)

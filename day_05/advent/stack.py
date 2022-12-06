class Stack:
    def __init__(self, number: int):
        self._number = number
        self._crates = []

    @property
    def number(self) -> int:
        return self._number

    @property
    def crates(self) -> list[str]:
        return self._crates

    def add_crate(self, *char: str):
        self._crates.extend(char)

    def pop_crate(self) -> str:
        return self._crates.pop()

    @property
    def top_crate(self) -> str:
        return self._crates[-1:][0]

    def __repr__(self):
        return f'Stack: {self._number}'

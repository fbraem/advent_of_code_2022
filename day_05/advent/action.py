from advent.stacks import Stacks


class Action:
    def __init__(self, count: int, current: int, to: int):
        self._count = count
        self._current = current
        self._to = to

    @property
    def count(self):
        return self._count

    @property
    def current(self):
        return self._current

    @property
    def to(self):
        return self._to

    def execute(self, stacks: Stacks):
        source = stacks.find_by_number(self._current)
        target = stacks.find_by_number(self._to)
        for i in range(0, self._count):
            crate = source.pop_crate()
            target.add_crate(crate)

    def execute_contain_order(self, stacks: Stacks):
        source = stacks.find_by_number(self._current)
        target = stacks.find_by_number(self._to)
        crates = []
        for i in range(0, self._count):
            crates.insert(0, source.pop_crate())

        for crate in crates:
            target.add_crate(crate)

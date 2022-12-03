from advent.strategy_guide import StrategyGuide


class StrategyGuideImporter:
    def __init__(self):
        self._strategy_guide = StrategyGuide()

    @property
    def strategy_guide(self) -> StrategyGuide:
        return self._strategy_guide

    def read_file(self, path: str):
        self.strategy_guide.clear()
        with open(path) as file:
            for line in file.readlines():
                parts = line.rsplit()
                self._strategy_guide.add_strategy((parts[0], parts[1]))

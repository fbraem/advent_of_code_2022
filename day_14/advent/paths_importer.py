from advent.path import Path
from advent.paths import Paths


class PathsImporter:
    def __init__(self):
        self._paths = Paths()

    @property
    def paths(self) -> Paths:
        return self._paths

    def read_file(self, path):
        with open(path) as file:
            lines = [line.rstrip() for line in file]
            for line in lines:
                path = Path()
                coordinates = line.split(' -> ')
                for coordinate in coordinates:
                    x, y = coordinate.split(',')
                    path.add_coordinate((int(x), int(y)))
                self._paths.add_path(path)

from typing import Tuple

from advent.sensor import Sensor


class Grid:
    def __init__(self, sensors: list[Sensor]):
        self._sensors = sensors

    def get_min_x(self) -> int:
        return min([sensor.min_x for sensor in self._sensors])

    def get_min_y(self) -> int:
        return min([sensor.min_y for sensor in self._sensors])

    def get_max_x(self) -> int:
        return max([sensor.max_x for sensor in self._sensors])

    def get_max_y(self) -> int:
        return max([sensor.max_y for sensor in self._sensors])

    def __str__(self) -> str:
        min_x = self.get_min_x()
        max_x = self.get_max_x() + 1
        min_y = self.get_min_y()
        max_y = self.get_max_y() + 1

        sensors = [sensor.position for sensor in self._sensors]
        beacons = [sensor.nearest_beacon_position for sensor in self._sensors]

        result = ''
        for y in range(min_y, max_y):
            result += f'{y:3} '
            for x in range(min_x, max_x):
                if (x, y) in sensors:
                    result += 'S'
                elif (x, y) in beacons:
                    result += 'B'
                elif self.is_position_covered((x, y)):
                    result += '#'
                else:
                    result += '.'

            result += '\n'

        return result

    def is_position_covered(self, position: Tuple[int, int]) -> bool:
        for sensor in self._sensors:
            if sensor.is_position_covered(position):
                return True
        return False

    def count_blocked_beacon_in_row(self, y: int) -> int:
        min_x = self.get_min_x()
        max_x = self.get_max_x() + 1

        sensors = [sensor.position for sensor in self._sensors]
        beacons = [sensor.nearest_beacon_position for sensor in self._sensors]

        count = 0
        for x in range(min_x, max_x):
            if self.is_position_covered((x, y)):
                if (x, y) not in sensors and (x, y) not in beacons:
                    count += 1

        return count

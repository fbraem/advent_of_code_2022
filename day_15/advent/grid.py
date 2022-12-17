from typing import Tuple

from advent.sensor import Sensor


class Grid:
    def __init__(self, sensors: list[Sensor]):
        self._sensors = sensors

    def get_min_x(self) -> int:
        sensor_coverage = []
        [sensor_coverage.extend(self.get_sensor_coverage(sensor.position)) for sensor in self._sensors]
        return min(
            [sensor.position[0] for sensor in self._sensors] +
            [sensor.nearest_beacon_position[0] for sensor in self._sensors] +
            [pos[0] for pos in sensor_coverage]
        )

    def get_min_y(self) -> int:
        sensor_coverage = []
        [sensor_coverage.extend(self.get_sensor_coverage(sensor.position)) for sensor in self._sensors]
        return min(
            [sensor.position[1] for sensor in self._sensors] +
            [sensor.nearest_beacon_position[1] for sensor in self._sensors] +
            [pos[1] for pos in sensor_coverage]
        )

    def get_max_x(self) -> int:
        sensor_coverage = []
        [sensor_coverage.extend(self.get_sensor_coverage(sensor.position)) for sensor in self._sensors]
        return max(
            [sensor.position[0] for sensor in self._sensors] +
            [sensor.nearest_beacon_position[0] for sensor in self._sensors] +
            [pos[0] for pos in sensor_coverage]
        )

    def get_max_y(self) -> int:
        sensor_coverage = []
        [sensor_coverage.extend(self.get_sensor_coverage(sensor.position)) for sensor in self._sensors]
        return max(
            [sensor.position[1] for sensor in self._sensors] +
            [sensor.nearest_beacon_position[1] for sensor in self._sensors] +
            [pos[1] for pos in sensor_coverage]
        )

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
                elif any([(x, y) in self.get_sensor_coverage(sensor.position) for sensor in self._sensors]):
                    result += '#'
                else:
                    result += '.'

            result += '\n'

        return result

    def get_sensor_coverage(self, sensor_position: Tuple[int, int]) -> list[Tuple[int, int]]:
        sensor_coverage = []
        for sensor in self._sensors:
            if sensor_position == sensor.position:
                return sensor.calc_coverage()
        return sensor_coverage

    def count_blocked_beacon_in_row(self, y: int) -> int:
        min_x = self.get_min_x()
        max_x = self.get_max_x() + 1

        sensors = [sensor.position for sensor in self._sensors]
        beacons = [sensor.nearest_beacon_position for sensor in self._sensors]

        count = 0
        for x in range(min_x, max_x):
            if any([(x, y) in self.get_sensor_coverage(sensor.position) for sensor in self._sensors]):
                if (x, y) not in sensors and (x, y) not in beacons:
                    count += 1

        return count

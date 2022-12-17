import re

from advent.sensor import Sensor


class SensorsImporter:
    def __init__(self):
        self._sensors = []

    @property
    def sensors(self) -> list[Sensor]:
        return self._sensors

    def read_file(self, path: str):
        with open(path) as file:
            for line in file:
                sensor_part, beacon_part = line.rstrip().split(':')
                sensor_positions = re.findall(r'x=(-?\d*),\sy=(-?\d*)', sensor_part)
                beacon_positions = re.findall(r'x=(-?\d*),\sy=(-?\d*)', beacon_part)
                if sensor_positions and beacon_positions:
                    for sensor_position, beacon_position in zip(sensor_positions, beacon_positions):
                        sensor = Sensor(
                            (int(sensor_position[0]), int(sensor_position[1])),
                            (int(beacon_position[0]), int(beacon_position[1])),
                        )
                        self._sensors.append(sensor)

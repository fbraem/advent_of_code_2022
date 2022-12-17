from typing import Tuple


class Sensor:
    def __init__(self, pos: Tuple[int, int], nearest_beacon_pos: Tuple[int, int]):
        self._pos = pos
        self._nearest_beacon_pos = nearest_beacon_pos

    @property
    def position(self) -> Tuple[int, int]:
        return self._pos

    @property
    def nearest_beacon_position(self) -> Tuple[int, int]:
        return self._nearest_beacon_pos

    @property
    def distance_sensor_beacon(self):
        return (
            self.nearest_beacon_position[0] - self._pos[0],
            self.nearest_beacon_position[1] - self._pos[1]
        )

    def calc_coverage(self) -> list[Tuple[int, int]]:
        coverage = []
        distance = self.distance_sensor_beacon

        line_length = abs(distance[0]) + abs(distance[1])
        start = (self._pos[0], self._pos[1] - line_length)
        end = (self._pos[0], self._pos[1] + line_length)

        # Fill the coverage from top to bottom in one loop
        for row in range(0, line_length + 1):
            for col in range(0, row * 2 + 1):
                x = start[0] + col - row
                top_y = start[1] + row
                bottom_y = end[1] - row
                coverage.append((x, start[1] + row))
                if top_y != bottom_y:
                    coverage.append((x, end[1] - row))

        return coverage

    def __str__(self):
        return f'Sensor at x={self._pos[0]}, y={self._pos[1]}:' \
               f' closest beacon is at x={self._nearest_beacon_pos[0]}, ' \
               f'y={self._nearest_beacon_pos[1]}'

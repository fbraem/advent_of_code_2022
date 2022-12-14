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

    @property
    def min_x(self) -> int:
        distance = self.distance_sensor_beacon
        line_length = abs(distance[0]) + abs(distance[1])
        return self._pos[0] - line_length

    @property
    def max_x(self) -> int:
        distance = self.distance_sensor_beacon
        line_length = abs(distance[0]) + abs(distance[1])
        return self._pos[0] + line_length

    @property
    def min_y(self) -> int:
        distance = self.distance_sensor_beacon
        line_length = abs(distance[0]) + abs(distance[1])
        return self._pos[1] - line_length

    @property
    def max_y(self) -> int:
        distance = self.distance_sensor_beacon
        line_length = abs(distance[0]) + abs(distance[1])
        return self._pos[1] + line_length

    def is_position_covered(self, position: Tuple[int, int]) -> bool:
        distance = self.distance_sensor_beacon
        line_length = abs(distance[0]) + abs(distance[1])

        distance_pos_x = abs(self._pos[0] - position[0])
        distance_pos_y = abs(self._pos[1] - position[1])

        max_right_x = line_length - abs(self._pos[1] - position[1])

        left = (
            self._pos[0] - line_length + distance_pos_y,
            position[1]
        )
        right = (
            min(self._pos[0] + distance_pos_x, self._pos[0] + max_right_x),
            position[1]
        )

        if left == right:
            return position == left

        return left[0] <= position[0] <= right[0]

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

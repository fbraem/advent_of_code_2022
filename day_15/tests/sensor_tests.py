import unittest

from advent.sensor import Sensor


class SensorTests(unittest.TestCase):
    def test_inside(self):
        sensor = Sensor((8, 7), (2, 10))

        self.assertTrue(sensor.is_position_covered((8, -2)), 'This position should be covered')
        self.assertTrue(sensor.is_position_covered((8, 16)), 'This position should be covered')
        self.assertTrue(sensor.is_position_covered((-1, 7)), 'This position should be covered')
        self.assertTrue(sensor.is_position_covered((8, 7)), 'This position should be covered')
        self.assertTrue(sensor.is_position_covered((8, -1)), 'This position should be covered')
        self.assertTrue(sensor.is_position_covered((9, -1)), 'This position should be covered')
        self.assertTrue(sensor.is_position_covered((7, -1)), 'This position should be covered')
        self.assertTrue(sensor.is_position_covered((5, 5)), 'This position should be covered')
        self.assertTrue(sensor.is_position_covered((16, 8)), 'This position should be covered')
        self.assertFalse(sensor.is_position_covered((9, -2)), 'This position should not be covered')

    def test_distance(self):
        sensor = Sensor((8, 7), (2, 10))
        self.assertEqual((-6, 3), sensor.distance_sensor_beacon, 'The distance should be (-6, 3)')

    def test_min_x(self):
        sensor = Sensor((8, 7), (2, 10))
        print(sensor.min_x)

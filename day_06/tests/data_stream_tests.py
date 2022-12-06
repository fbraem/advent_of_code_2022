import unittest

from advent.data_stream import DataStream


class DataStreamTest(unittest.TestCase):
    def test_detect_start_of_packet(self):
        data_stream = DataStream('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
        self.assertEqual(data_stream.detect_marker(4), 7)

        data_stream = DataStream('bvwbjplbgvbhsrlpgdmjqwftvncz')
        self.assertEqual(data_stream.detect_marker(4), 5)

        data_stream = DataStream('nppdvjthqldpwncqszvftbrmjlhg')
        self.assertEqual(data_stream.detect_marker(4), 6)

        data_stream = DataStream('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
        self.assertEqual(data_stream.detect_marker(4), 10)

        data_stream = DataStream('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
        self.assertEqual(data_stream.detect_marker(4), 11)

    def test_detect_start_of_message(self):
        data_stream = DataStream('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
        self.assertEqual(data_stream.detect_marker(14), 19)

        data_stream = DataStream('bvwbjplbgvbhsrlpgdmjqwftvncz')
        self.assertEqual(data_stream.detect_marker(14), 23)

        data_stream = DataStream('nppdvjthqldpwncqszvftbrmjlhg')
        self.assertEqual(data_stream.detect_marker(14), 23)

        data_stream = DataStream('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
        self.assertEqual(data_stream.detect_marker(14), 29)

        data_stream = DataStream('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
        self.assertEqual(data_stream.detect_marker(14), 26)

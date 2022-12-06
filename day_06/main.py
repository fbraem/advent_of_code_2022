from advent.data_stream import DataStream

with open('./files/day6_input') as file:
    data = file.read()

    data_stream = DataStream(data)
    print('First package-marker at:', data_stream.detect_marker(4))
    print('First start-of-message marker at:', data_stream.detect_marker(14))

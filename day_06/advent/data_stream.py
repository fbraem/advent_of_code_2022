class DataStream:
    def __init__(self, buffer: str):
        self._buffer = buffer

    def detect_marker(self, size: int) -> int:
        start = 0
        for pos in range(0, len(self._buffer)):
            marker = self._buffer[pos:pos + size]
            unique_chars = set(list(marker))
            if len(unique_chars) == size:
                start = pos + size
                break

        return start

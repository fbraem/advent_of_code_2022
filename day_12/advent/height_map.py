import heapq
from typing import Tuple, Optional


class HeightMap:
    def __init__(self):
        self._map = []
        self._start = ()
        self._end = ()

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def add_row(self, heights: str):
        row = []

        for index, char in enumerate(heights):
            if char == 'S':
                self._start = len(self._map), index
                row.append(0)
            elif char == 'E':
                self._end = len(self._map), index
                row.append(25)
            else:
                row.append(ord(char) - 97)
        self._map.append(row)

    def __get_nodes(self):
        nodes = []
        for r, row in enumerate(self._map):
            for c, col in enumerate(row):
                nodes.append((r, c))
        return nodes

    def get_height(self, node: Tuple[int, int]) -> int:
        return self._map[node[0]][node[1]]

    @property
    def row_count(self):
        return len(self._map)

    def __get_neighbours(self, node):
        current_height = self.get_height(node)

        neighbours = []
        if node[0] > 0:
            up_node = (node[0] - 1, node[1])
            if self.get_height(up_node) - current_height <= 1:
                neighbours.append(up_node)
        if node[0] < self.row_count - 1:
            down_node = (node[0] + 1, node[1])
            if self.get_height(down_node) - current_height <= 1:
                neighbours.append(down_node)
        if node[1] < len(self._map[0]) - 1:
            right_node = (node[0], node[1] + 1)
            if self.get_height(right_node) - current_height <= 1:
                neighbours.append(right_node)
        if node[1] > 0:  # We assume all rows have the same length
            left_node = (node[0], node[1] - 1)
            if self.get_height(left_node) - current_height <= 1:
                neighbours.append(left_node)

        return neighbours

    def get_shortest_route(self, start: Optional[Tuple[int, int]] = None):
        """Dijkstra algorithm implementation
        """
        nodes = self.__get_nodes()
        distances = {node: 10000000 for node in nodes}
        if start is None:
            q = [(0, self._start)]
        else:
            q = [(0, start)]
        distances[self._start] = 0

        while q:
            d, min_node = heapq.heappop(q)
            for neighbour in self.__get_neighbours(min_node):
                if distances[neighbour] > d + 1:
                    new_dist = d + 1
                    distances[neighbour] = new_dist
                    heapq.heappush(q, (new_dist, neighbour))

        return distances[self._end]

    def part_2(self):
        shorted_routes = []
        for node in self.__get_nodes():
            height = self.get_height(node)
            if height == 0:
                shorted_routes.append(self.get_shortest_route(node))
        return min(shorted_routes)

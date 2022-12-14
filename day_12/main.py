from advent.height_map import HeightMap

height_map = HeightMap()
with open('./files/day12_input') as file:
    for line in file:
        height_map.add_row(line.rstrip())

print(height_map.get_shortest_route())
print(height_map.part_2())

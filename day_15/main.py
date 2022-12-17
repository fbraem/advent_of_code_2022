from advent.grid import Grid
from advent.sensors_importer import SensorsImporter

sensors_importer = SensorsImporter()
sensors_importer.read_file('./files/day15_example')
for sensor in sensors_importer.sensors:
    print(sensor)

grid = Grid(sensors_importer.sensors)
print('min x', grid.get_min_x())
print('max x', grid.get_max_x())
print('sum x', abs(grid.get_min_x()) + abs(grid.get_max_x()))
print('min y', grid.get_min_y())
print('max y', grid.get_max_y())
print('sum y', abs(grid.get_min_y()) + abs(grid.get_max_y()))

print('Number of blocked positions for y=: 10', grid.count_blocked_beacon_in_row(10))
print(grid)

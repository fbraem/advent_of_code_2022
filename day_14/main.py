from advent.grid import Grid
from day_14.advent.paths_importer import PathsImporter

importer = PathsImporter()
importer.read_file('./files/day14_input')

grid = Grid(importer.paths.copy())

count = 0
while True:
    moves = grid.drop_sand((500, 0))
    if moves == 0:
        break
    count += 1

print(grid)
print('Number of moves:', count)

grid = Grid(importer.paths.copy(), True)

count = 0
while True:
    moves = grid.drop_sand((500, 0))
    if moves == 0:
        break
    count += 1
print(grid)
print('Number of moves:', count + 1)

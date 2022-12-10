from advent.grid import Grid
from advent.rope import Rope

grid = Grid(Rope((1, 1), (1, 1)))
with open('./files/day9_input') as file:
    for line in file:
        direction, step = line.rstrip().split()
        grid.move_rope(direction, int(step))

print('visits', grid.number_of_visits)

start_knot = (500, 500)
grid = Grid(Rope(*(start_knot,) * 10))
with open('./files/day9_input') as file:
    for line in file:
        direction, step = line.rstrip().split()
        grid.move_rope(direction, int(step))
print('visits', grid.number_of_visits)

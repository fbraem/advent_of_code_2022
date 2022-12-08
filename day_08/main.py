from advent.forest import Forest

forest = Forest()
with open('./files/day8_input') as file:
    for line in file:
        forest.add_row_from_string(line.rstrip())
print('Number of visible trees:', forest.count_visible_trees())
print('Max scenic score: ', forest.get_highest_scenic_score())

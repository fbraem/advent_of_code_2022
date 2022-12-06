from advent.rucksack_importer import RucksackImporter

importer = RucksackImporter()
importer.read_file('./files/day3_input')

print('Number of rucksacks:', len(importer.rucksacks))

sum_of_shared_priorities = 0
for rucksack in importer.rucksacks:
    item = rucksack.find_shared_item()
    if item is not None:
        sum_of_shared_priorities += item.priority
print('The sum of shared priorities', sum_of_shared_priorities)

sum_of_badge_priorities = 0
groups = importer.get_groups()
print('Number of groups:', len(groups))
for group in groups:
    badge = group.find_badge()
    if badge:
        sum_of_badge_priorities += badge.priority
print('The sum of badge priorities', sum_of_badge_priorities)

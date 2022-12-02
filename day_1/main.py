import itertools

from advent.elf_importer import ElfImporter

importer = ElfImporter()
importer.read_file('./files/day1_input')
print('Number of elves:', importer.elves.count)

elf = importer.elves.get_elf_with_most_calories()
if elf is not None:
    print('Elf carrying the most calories:', elf.carried_calories)

print('Top 3:')
elves = importer.elves.sort()
total_top_3 = 0
for elf in itertools.islice(elves, 0, 3):
    total_top_3 += elf.carried_calories
    print(elf.carried_calories)
print('Sum of top3: ', total_top_3)

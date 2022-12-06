from advent.pairs_importer import PairsImporter

importer = PairsImporter()
importer.read_file('./files/day4_input')
print('Number of pairs:', len(importer.pairs))

fully_contained_count = 0
overlap_count = 0
for pair in importer.pairs:
    if pair.is_fully_contained():
        fully_contained_count += 1
    if pair.get_overlaps():
        overlap_count += 1
print('Number of fully contained pairs:', fully_contained_count)
print('Number of overlaps:', overlap_count)

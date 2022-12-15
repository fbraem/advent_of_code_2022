from advent.pair_importer import PairImporter

importer = PairImporter()
importer.read_file('./files/day13_input')

print('Sum of right order indices:', importer.compare())
# Don't know why, but after adding sorting, part 1 is wrong...
decoder_key = importer.sort()
print('Decoder Key:', decoder_key[0] * decoder_key[1])

from advent.notes_importer import NotesImporter

importer = NotesImporter()
importer.read_file('./files/day11_input')

for i in range(0, 20):
    importer.monkeys.play_round()

for monkey in importer.monkeys:
    print(monkey)
print('Monkey business: ', importer.monkeys.monkey_business)

importer = NotesImporter()
importer.read_file('./files/day11_input')

for i in range(0, 10000):
    importer.monkeys.play_round(change_worry=False)

for monkey in importer.monkeys:
    print(monkey)
print('Monkey business: ', importer.monkeys.monkey_business)

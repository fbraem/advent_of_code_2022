from advent.strategy_guide_importer import StrategyGuideImporter

importer = StrategyGuideImporter()
importer.read_file('./files/day2_input')

result = importer.strategy_guide.play()
print(result)
result = importer.strategy_guide.play_part_2()
print(result)

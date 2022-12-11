from advent.cpu import CPU
from advent.instruction import InstructionFactory
from advent.instruction_importer import InstructionImporter

importer = InstructionImporter()
importer.read_file('./files/day10_input')
cpu = CPU()
for instruction in importer.instructions:
    cpu.execute(InstructionFactory.create_instruction(*instruction))

print('The sum of these six signal strengths', sum(cpu.signal_strengths))

for line in cpu.crt:
    print(line)

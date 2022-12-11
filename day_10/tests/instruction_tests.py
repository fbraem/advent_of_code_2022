import unittest

from advent.cpu import CPU
from advent.instruction import Noop, AddX


class InstructionTests(unittest.TestCase):
    def test_noop(self):
        cpu = CPU()
        noop = Noop()

        cpu.execute(noop)

        self.assertEqual(1, cpu.register, 'The CPU register should be 1')
        self.assertEqual(1, cpu.cycles, 'The CPU cycles should be 1')

    def test_addx(self):
        cpu = CPU()
        addx = AddX(5)

        cpu.execute(addx)

        self.assertEqual(6, cpu.register, 'The CPU register should be 6')
        self.assertEqual(2, cpu.cycles, 'The CPU cycles should be 2')

    def test_small_program(self):
        cpu = CPU()
        instructions = [
            Noop(),
            AddX(3),
            AddX(-5)
        ]
        for instruction in instructions:
            cpu.execute(instruction)

        self.assertEqual(-1, cpu.register, 'The CPU register should be -1')
        self.assertEqual(5, cpu.cycles, 'The CPU cycles should be 5')

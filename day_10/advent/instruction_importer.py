class InstructionImporter:
    def __init__(self):
        self._instructions = []

    @property
    def instructions(self):
        return self._instructions

    def read_file(self, path: str):
        with open(path) as file:
            for line in file:
                instruction_line = line.rstrip()
                parts = instruction_line.split(' ')
                if len(parts) > 1:
                    self._instructions.append((parts[0], parts[1]))
                else:
                    self._instructions.append((parts[0],))

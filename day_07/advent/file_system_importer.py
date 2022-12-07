from advent.file_system import FileSystem


class FileSystemImporter:
    def __init__(self):
        self._fs = FileSystem()

    def read_file(self, path: str) -> FileSystem:
        with open(path) as file:
            for line in file:
                stripped_line = line.rstrip()
                if len(stripped_line) == 0:
                    continue

                if stripped_line[0] == '$':  # A command starts with $
                    self.__process_command(stripped_line[1:])
                else:
                    self.__process_object(stripped_line)

        return self._fs

    def __process_command(self, command_line: str):
        command, *args = command_line.split()
        match command:
            case 'cd':
                if len(args) == 0:
                    raise RuntimeError('A cd command without an argument is invalid')
                current = self._fs.cd(args[0])
                if current is None:
                    raise RuntimeError(f'Failed to change directory to {args[0]}')
            case 'ls':
                # We don't need to do anything here...
                return
            case _:
                raise RuntimeError(f'Unknown command ${command}')

    def __process_object(self, object_line):
        object_parts = object_line.split(' ')
        if object_parts[0] == 'dir':
            self._fs.add_directory(object_parts[1])
        else:
            self._fs.add_file(object_parts[1], int(object_parts[0]))

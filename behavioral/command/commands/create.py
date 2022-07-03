from behavioral.command.commands.base_command import BaseCommand
from behavioral.command.commands.delete import DeleteFileCommand


class CreateFileCommand(BaseCommand):
    def __init__(self, path: str, initial_content: str, verbose=True):
        super().__init__(verbose)
        self._path = path
        self._initial_content = initial_content

    def execute(self):
        self.log(f"[CREATE FILE] {self._path}")
        with open(self._path, mode="w", encoding="utf-8") as file:
            file.write(self._initial_content)

    def undo(self):
        self.log(f"[UNDO - CREATE FILE] {self._path} with header {self._header}")
        delete = DeleteFileCommand(self._path)
        delete.execute()

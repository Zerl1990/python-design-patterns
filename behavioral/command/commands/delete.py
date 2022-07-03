import os

from behavioral.command.commands.base_command import BaseCommand
from behavioral.command.commands.read import ReadFileCommand


class DeleteFileCommand(BaseCommand):
    def __init__(self, path: str, verbose: bool = True):
        super().__init__(verbose)
        self._path = path
        self._bk = None

    def execute(self):
        self.log(f"[DELETE FILE] {self._path}")
        self._bk = ReadFileCommand(self._path, False).execute()
        os.remove(self._path)

    def undo(self):
        self.log(f"[UNDO - DELETE FILE] {self._path}")
        with open(self._path, mode="w", encoding="utf-8") as file:
            file.write(self._bk)

import os

from behavioral.command.commands.base_command import BaseCommand


class RenameFileCommand(BaseCommand):
    def __init__(self, src: str, dst: str, verbose: bool = True):
        super().__init__(True)
        self._src = src
        self._dst = dst

    def execute(self):
        self.log(f"[RENAME FILE] {self._src} -> {self._dst}")
        os.rename(self._src, self._dst)

    def undo(self):
        self.log(f"[UNDO - RENAME FILE] {self._dst} -> {self._src}")
        os.rename(self._dst, self._src)

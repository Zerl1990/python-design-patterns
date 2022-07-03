from behavioral.command.commands.base_command import BaseCommand


class ReadFileCommand(BaseCommand):
    def __init__(self, path: str, verbose: bool = True):
        super().__init__(verbose)
        self._path = path

    def execute(self) -> str:
        self.log(f"[READ FILE] {self._path}")
        with open(self._path, mode="r", encoding="utf-8") as file:
            return file.read()

    def undo(self):
        self.log(f"[UNDO - READ FILE] NO IMPLEMENTED - {self._path}")

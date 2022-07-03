from abc import abstractmethod


class BaseCommand:
    def __init__(self, verbose: bool = True):
        self._verbose = verbose

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    def log(self, msg: str):
        if self._verbose:
            print(msg)

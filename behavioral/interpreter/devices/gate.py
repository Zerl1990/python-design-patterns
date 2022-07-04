

class Gate:
    def __init__(self, name: str):
        self.name = name

    def open(self, *args):
        print(f"[GATE][OPEN][{self.name}]: {args}")

    def close(self, *args):
        print(f"[GATE][CLOSE][{self.name}]: {args}")

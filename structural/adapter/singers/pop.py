
class PopSinger:
    def __init__(self, name: str):
        self._name = name

    def sing(self, *args, **kwargs):
        print(f"Pop signers {self._name} starts to sign")

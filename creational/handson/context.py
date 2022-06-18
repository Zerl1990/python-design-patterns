from creational.handson.singleton_type import SingletonType


class Context(metaclass=SingletonType):
    def __init__(self, name: str, version: str, default_delay: int):
        self._name = name
        self._version = version
        self._default_delay = default_delay

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def default_delay(self) -> int:
        return self._default_delay

    def __str__(self):
        return f"Name: {self.name}, Version: {self.version}, Default Delay: {self.default_delay}"

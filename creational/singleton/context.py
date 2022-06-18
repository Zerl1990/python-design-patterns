from creational.singleton.singleton_type import SingletonType


class Context(metaclass=SingletonType):
    def __int__(self):
        self.name = None
        self.version = None


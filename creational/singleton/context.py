from creational.singleton.SingletonType import SingletonType


class Context(metaclass=SingletonType):
    def __int__(self):
        self.name = None
        self.version = None


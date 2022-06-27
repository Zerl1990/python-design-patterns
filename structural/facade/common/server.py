import abc


class Server(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def boot(self):
        pass

    @abc.abstractmethod
    def kill(self, restart=True):
        pass

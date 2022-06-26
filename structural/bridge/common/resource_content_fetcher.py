import abc


class ResourceContentFetcher(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fetch(self, path):
        pass

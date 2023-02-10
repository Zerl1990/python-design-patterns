from abc import abstractmethod, ABC
from structural.bridge.common.resource_content_fetcher import ResourceContentFetcher


class ResourceContent(ABC):
    @abstractmethod
    def show_content(self, path):
        pass

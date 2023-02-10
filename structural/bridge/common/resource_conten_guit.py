from structural.bridge.common.resource_content import ResourceContent
from structural.bridge.common.resource_content_fetcher import ResourceContentFetcher


class ResourceContentUI(ResourceContent):
    def __init__(self, imp: ResourceContentFetcher):
        self._imp = imp  # Contains - Composicion

    def show_content(self, path):
        content = self._imp.fetch(path)
        print(content, end="-----")

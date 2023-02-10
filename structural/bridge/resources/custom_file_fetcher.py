from structural.bridge.common.resource_content_fetcher import ResourceContentFetcher


class CustomFileFetcher(ResourceContentFetcher):
    def fetch(self, path: str) -> str:
        with open(path) as f:
            return f.readline()

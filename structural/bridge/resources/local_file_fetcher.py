from structural.bridge.common.resource_content_fetcher import ResourceContentFetcher


class LocalFileFetcher(ResourceContentFetcher):
    def fetch(self, path):
        with open(path) as f:
            print(f.read())

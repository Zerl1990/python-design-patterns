import requests
from structural.bridge.common.resource_content_fetcher import ResourceContentFetcher


class URLFetcher(ResourceContentFetcher):
    def fetch(self, path):
        resp = requests.get(path)
        if resp.status_code == 200:
            print(resp.content)

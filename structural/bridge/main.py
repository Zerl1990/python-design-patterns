from structural.bridge.common.resource_content import ResourceContent
from structural.bridge.resources.local_file_fetcher import LocalFileFetcher
from structural.bridge.resources.url_fetcher import URLFetcher


if __name__ == "__main__":
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content("http://python.org")

    print("=" * 80)

    local_fetcher = LocalFileFetcher()
    iface = ResourceContent(local_fetcher)
    iface.show_content("./test_file.txt")

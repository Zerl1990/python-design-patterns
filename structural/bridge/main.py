from structural.bridge.common.resource_conten_cmdt import ResourceContentCmd
from structural.bridge.common.resource_conten_guit import ResourceContentUI
from structural.bridge.common.resource_content import ResourceContent
from structural.bridge.resources.custom_file_fetcher import CustomFileFetcher
from structural.bridge.resources.json_file_fetcher import JsonFileFetcher
from structural.bridge.resources.local_file_fetcher import LocalFileFetcher
from structural.bridge.resources.url_fetcher import URLFetcher


if __name__ == "__main__":
    json_fetcher = JsonFileFetcher()
    iface = ResourceContentCmd(json_fetcher)
    iface.show_content("./test.json")

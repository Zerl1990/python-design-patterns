import json
from json import JSONDecodeError

from structural.bridge.common.resource_content_fetcher import ResourceContentFetcher


class JsonFileFetcher(ResourceContentFetcher):
    def fetch(self, path: str) -> str:
        if not path.endswith("json"):
            raise ValueError(f"Invalid data type, expected JSON, received: {path}")
        with open(path) as f:
            json_data = None
            try:
                json_data = json.load(f)
            except JSONDecodeError:
                print(f"[WARN] - Invalid Json for {path}")
            finally:
                return json_data

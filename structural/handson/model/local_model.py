

class TwitterLocalModel:
    def __init__(self):
        self.name = "LOCAL MODEL"

    def search_all(self, value: str):
        print(f"[{self.name}] - SEARCH ALL: {value}")

    def search_recent(self, value: str):
        print(f"[{self.name}] - SEARCH RECENT: {value}")

    def follow(self, user: str):
        print(f"[{self.name}] - FOLLOW: {user}")

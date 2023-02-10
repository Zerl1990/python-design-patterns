from structural.facade.common.server import Server
from structural.facade.common.state import State


class FileServer(Server):
    def __init__(self):
        self.name = "File Server"
        self.state = State.NEW

    def boot(self):
        print(f"Booting the {self.name}")
        self.state = State.RUNNING

    def create_file(self, user: str, name: str, permission: int):
        print(f"{self.name} trying to create the file {name} for user {user} with permission {permission}")

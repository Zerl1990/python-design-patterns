from structural.facade.common.server import Server
from structural.facade.common.state import State


class ProcessServer(Server):
    def __init__(self):
        self.name = "Process Server"
        self.state = State.NEW

    def boot(self):
        print(f"Booting the {self.name}")
        self.state = State.RUNNING

    def kill(self, restart: bool = True):
        print(f"Killing {self.name}")
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_process(self, user: str, name: str):
        print(f"{self.name} trying to create the process {name} for user {user}")

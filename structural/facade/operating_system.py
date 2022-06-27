from structural.facade.servers.file_server import FileServer
from structural.facade.servers.process_server import ProcessServer


class OperatingSystem:
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [server.boot() for server in (self.fs, self.ps)]

    def create_file(self, user: str, name: str, permission: int):
        self.fs.create_file(user, name, permission)

    def create_process(self, user: str, name: str):
        self.ps.create_process(user, name)

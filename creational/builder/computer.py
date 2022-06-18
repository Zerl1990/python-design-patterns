import uuid


class Computer:
    def __init__(self):
        self.serial = uuid.uuid1()
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = [
            f"Serial Number: {self.serial}",
            f"Memory: {self.memory} GB",
            f"Hard Disk: {self.hdd} GB",
            f"Graphics Card: {self.gpu}",
        ]
        return "\n".join(info)

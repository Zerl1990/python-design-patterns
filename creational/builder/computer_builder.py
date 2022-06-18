from creational.builder.computer import Computer


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_memory(self, amount: int):
        self.computer.memory = amount

    def configure_hdd(self, amount: int):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model: str):
        self.computer.gpu = gpu_model

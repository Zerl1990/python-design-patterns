from creational.builder.computer_builder import ComputerBuilder


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory: int, hdd: int, gpu: str):
        self.builder = ComputerBuilder()
        # STEPS
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    @property
    def computer(self):
        return self.builder.computer

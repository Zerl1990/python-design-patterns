from creational.builder.hardware_engineer import HardwareEngineer

if __name__ == "__main__":
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu="GeForce GTX 650 Ti")
    computer = engineer.computer
    print(computer)


from structural.facade.operating_system import OperatingSystem

if __name__ == "__main__":
    os = OperatingSystem()
    os.start()
    os.create_file("luis", "hello", 5)
    os.create_process("luis", "ls")

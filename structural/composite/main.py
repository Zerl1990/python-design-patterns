from structural.composite.developer import Developer
from structural.composite.manager import Manager

if __name__ == "__main__":
    m1 = Manager("M1", "M1", 1000)

    m2 = Manager("M2", "M2", 900)
    dev1 = Developer("DEV1", "DEV1", 800)
    dev2 = Developer("DEV2", "DEV2", 800)
    dev3 = Developer("DEV3", "DEV3", 800)
    m2.add_employee(dev1)
    m2.add_employee(dev2)
    m2.add_employee(dev3)
    m1.add_employee(m2)

    m3 = Manager("M3", "M3", 900)
    dev4 = Developer("DEV4", "DEV4", 800)
    dev5 = Developer("DEV5", "DEV5", 800)
    dev6 = Developer("DEV6", "DEV6", 800)
    m3.add_employee(dev4)
    m3.add_employee(dev5)
    m3.add_employee(dev6)
    m1.add_employee(m3)

    m1.show_details()

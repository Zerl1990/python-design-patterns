

class AirCondition:
    def __init__(self, name: str):
        self.name = name

    def on(self, *args):
        print(f"[AIR CONDITION][ON][{self.name}]: {args}")

    def off(self, *args):
        print(f"[AIR CONDITION][OFF][{self.name}]: {args}")

    def increase(self, *args):
        print(f"[AIR CONDITION][INCREASE][{self.name}]: {args}")

    def decrease(self, *args):
        print(f"[AIR CONDITION][DECREASE][{self.name}]: {args}")

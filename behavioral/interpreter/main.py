from behavioral.interpreter.devices.air_condition import AirCondition
from behavioral.interpreter.devices.gate import Gate
from behavioral.interpreter.interpreter import EventInterpreter

if __name__ == "__main__":
    devices = [
        Gate("Front Gate"),
        AirCondition("Room Air Condition"),
        AirCondition("Kitchen Air Condition")
    ]
    interpreter = EventInterpreter(devices)
    commands = [
        "Front Gate -> Open",
        "Front Gate -> Close",
        "Room Air Condition -> On",
        "Room Air Condition -> Increase -> 10",
        "Kitchen Air Condition -> Decrease -> 40"
    ]
    for command in commands:
        interpreter.execute(command)

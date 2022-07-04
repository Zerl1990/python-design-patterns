from collections import namedtuple


Event = namedtuple("Event", ["device", "action", "args"])


class EventInterpreter:

    def __init__(self, devices: dict):
        self._devices = {}
        for device in devices:
            self._devices[device.name.lower()] = device

    def parse(self, command: str) -> Event:
        """Parse an event command.

        :param command: Format: [DEVICE] -> [ACTION] -> [ARG1, ARG2]
        :return:
        """
        tokens = command.split("->")
        if len(tokens) < 2:
            raise ValueError(f"Invalid command: {command}")
        device, action = tokens[0].lower().strip(), tokens[1].lower().strip()
        args = tokens[2].split(",") if len(tokens) == 3 else []
        if device not in self._devices:
            raise RuntimeError(f"Device {device} not supported")
        if not hasattr(self._devices[device], action):
            raise RuntimeError(f"Device {device} does not support action {action}")
        return Event(device, action, args)

    def execute(self, command: str):
        event = self.parse(command)
        method = getattr(self._devices[event.device], event.action)
        method(*event.args)

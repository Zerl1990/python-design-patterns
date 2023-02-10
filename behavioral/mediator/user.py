

class User:
    def __init__(self, mediator, u_id: int, alias: str, status: str = "ACTIVE"):
        self._id = u_id
        self._alias = alias
        self._status = status
        self._mediator = mediator
        self._mediator.add_user(self)

    @property
    def status(self):
        return self._status

    def send_msg(self, msg: str, *args):
        self._mediator.send_message(msg, args)

    def receive_msg(self, msg: str):
        print(f"{self}[RECEIVE MESSAGE] {msg}")

    def __str__(self):
        return f"[USER][{self._id}][{self._status}][{self._alias}]"

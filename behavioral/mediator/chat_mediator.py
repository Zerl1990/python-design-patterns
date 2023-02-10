

class ChatMediator:
    def __init__(self):
        self._users = set()

    def add_user(self, user):
        self._users.add(user)

    def send_message(self, msg: str, *args):
        args = set(args)
        for user in self._users:
            if user in args and user.status == "ACTIVE":
                user.receive_msg(msg)
                break
        else:
            print("WARNING - USER NOT FOUND")

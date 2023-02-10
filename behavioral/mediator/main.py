from behavioral.mediator.chat_mediator import ChatMediator
from behavioral.mediator.user import User

if __name__ == "__main__":
    mediator = ChatMediator()
    userA = User(mediator, 1, "A")
    userB = User(mediator, 2, "B")
    userC = User(mediator, 3, "C")
    userD = User(mediator, 4, "D")
    userE = User(mediator, 5, "E")

    userA.send_msg("HELLO", userE, userD, userB)


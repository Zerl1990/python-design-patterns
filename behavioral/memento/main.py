from behavioral.memento.common.CareTaker import CareTaker
from behavioral.memento.position import Position

if __name__ == "__main__":
    position = Position()
    care_taker = CareTaker(position)

    for tmp in range(0, 11):
        position.x = tmp
        position.y = tmp
        print(position)
        care_taker.backup()

    print("==========BACKUPS============")
    while True:
        try:
            care_taker.undo()
            print(position)
        except IndexError:
            pass

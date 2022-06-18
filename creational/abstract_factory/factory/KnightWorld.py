from creational.abstract_factory.factory.AbstractWorld import AbstractWorld
from creational.abstract_factory.heroes.knight import Knight
from creational.abstract_factory.villains.dragon import Dragon


class KnightWorld(AbstractWorld):
    def __init__(self, player_name: str):
        self.player_name = player_name
        print(self)

    def __str__(self):
        return "\n\n\t------ Knight World ------"

    def create_hero(self) -> Knight:
        return Knight(self.player_name)

    def create_villain(self) -> Dragon:
        return Dragon()

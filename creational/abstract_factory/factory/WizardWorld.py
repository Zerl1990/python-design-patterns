from creational.abstract_factory.factory.AbstractWorld import AbstractWorld
from creational.abstract_factory.heroes.wizard import Wizard
from creational.abstract_factory.villains.ork import Ork


class WizardWorld(AbstractWorld):
    def __init__(self, player_name: str):
        self.player_name = player_name
        print(self)

    def __str__(self):
        return "\n\n\t------ Wizard World ------"

    def create_hero(self) -> Wizard:
        return Wizard(self.player_name)

    def create_villain(self) -> Ork:
        return Ork()

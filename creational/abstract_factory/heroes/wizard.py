from creational.abstract_factory.heroes.hero import Hero
from creational.abstract_factory.villains.villain import Villain


class Wizard(Hero):
    def __init__(self, name: str):
        super().__init__(name)

    def interact_with(self, villain: Villain):
        action = villain.action()
        print(f"{self} the Wizards battle against {villain} and {action}")

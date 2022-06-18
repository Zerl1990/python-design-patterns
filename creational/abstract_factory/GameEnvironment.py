from creational.abstract_factory.factory.AbstractWorld import AbstractWorld


class GameEnvironment:
    def __init__(self, factory: AbstractWorld):
        self.hero = factory.create_hero()
        self.villain = factory.create_villain()

    def play(self):
        self.hero.interact_with(self.villain)

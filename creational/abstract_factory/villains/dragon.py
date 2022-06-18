from creational.abstract_factory.villains.villain import Villain


class Dragon(Villain):
    def __str__(self):
        return "an evil Dragon"

    def action(self):
        return "kills it"

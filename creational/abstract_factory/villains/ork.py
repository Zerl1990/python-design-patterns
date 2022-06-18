from creational.abstract_factory.villains.villain import Villain


class Ork(Villain):
    def __str__(self):
        return "an evil Ork"

    def action(self):
        return "fights it"

from creational.abstract_factory.GameEnvironment import GameEnvironment
from creational.abstract_factory.factory.KnightWorld import KnightWorld
from creational.abstract_factory.factory.WizardWorld import WizardWorld

if __name__ == "__main__":
    name = input("Hello, what is your name?")
    g_type = None
    while not g_type:
        magic = input(f"Welcome {name}, Do you like magic (yes|no)?")
        if magic.lower() == "yes":
            g_type = "wizard"
        elif magic.lower() == "no":
            g_type = "knight"
        else:
            print("I did not hear you")
    game_factory = KnightWorld if g_type == "knight" else WizardWorld
    game = GameEnvironment(game_factory(name))
    game.play()

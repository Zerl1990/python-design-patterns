from behavioral.strategy.strategies.bike_strategy import BikeStrategy
from behavioral.strategy.strategies.walk_strategy import WalkStrategy


class App:
    def __init__(self):
        self._strategy = None

    def run(self):
        while True:
            distance = self.get_distance()
            strategy_name = self.get_strategy_name()
            self._strategy = BikeStrategy() if strategy_name == "bike" else WalkStrategy()
            self._strategy.execute(distance)

    def get_distance(self):
        distance_km = None
        while not distance_km:
            distance = input("Select a distance (KM): ")
            try:
                distance_km = int(distance)
            except Exception:
                pass
        return distance_km

    def get_strategy_name(self):
        name = None
        while name not in ("bike", "walk"):
            name = input("Select a valid options -  bike | walk: ")
        return name

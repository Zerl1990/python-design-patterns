from behavioral.strategy.strategies.strategy import Strategy


class BikeStrategy(Strategy):
    def execute(self, distance_km: int):
        print(f"Estimated time biking {distance_km * 2} minutes")

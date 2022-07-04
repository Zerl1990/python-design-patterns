from behavioral.strategy.strategies.strategy import Strategy


class WalkStrategy(Strategy):
    def execute(self, distance_km: int):
        print(f"Estimated time walking {distance_km * 10} minutes")

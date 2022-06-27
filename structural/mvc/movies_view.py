

class MoviesView:
    def __init__(self):
        self.name = "[TERMINAL VIEW]"

    def show(self, movie):
        print(f"{self.name} - Movie is: {movie}")

    def error(self, msg):
        print(f"{self.name} - Error: {msg}")

    def select_movie(self):
        return input(f"{self.name} - Which movie would you like [0-10]")

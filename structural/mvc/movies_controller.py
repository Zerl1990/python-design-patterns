from structural.mvc.movies_model import MoviesModel
from structural.mvc.movies_view import MoviesView


class MoviesController:
    def __init__(self):
        self.model = MoviesModel()
        self.view = MoviesView()

    def run(self):
        movie = None
        index = None
        while not movie:
            try:
                index = self.view.select_movie()
                index = int(index)
                movie = self.model.get_movie(index)
            except ValueError as err:
                self.view.error(f"Incorrect index: {index}")
        self.view.show(movie)

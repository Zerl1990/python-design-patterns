from structural.mvc.movies_controller import MoviesController

if __name__ == "__main__":
    controller = MoviesController()
    while True:
        controller.run()

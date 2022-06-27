

class MoviesModel:
    def __init__(self):
        # IMDB top 10 list.
        self._movies = [
            "El Padrino",
            "Sueño de fuga",
            "La lista de Schindler",
            "El toro salvaje",
            "Casablanca",
            "El cuidadano Kane",
            "Lo que el viento se llevo",
            "El mago de oz",
            "Atrapado sin salida",
            "Lawrence de Arabia",
        ]

    def get_movie(self, index):
        return self._movies[index] if 0 <= index < len(self._movies) else "Not Found"

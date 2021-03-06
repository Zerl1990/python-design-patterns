from structural.adapter.adapter import Adapter
from structural.adapter.comedians.anecdotal import AnecdotalComedian
from structural.adapter.singers.country import CountrySinger
from structural.adapter.singers.pop import PopSinger
from structural.adapter.singers.rock import RockSinger


ARTISTS = [
    CountrySinger("Blanca"),
    PopSinger("Leyli"),
    RockSinger("Dafne"),
    AnecdotalComedian("Luis")
]


def adapt_artists(artists: list) -> list:
    adapted_artists = []
    for artist in artists:
        if hasattr(artist, "talk"):
            adapted_methods = {"sing": artist.talk}
            artist = Adapter(artists, adapted_methods)
        adapted_artists.append(artist)
    return adapted_artists


def start_event(artists: list):
    """Function can not be modified!!!"""
    for artist in artists:
        artist.sing()


if __name__ == "__main__":
    start_event(adapt_artists(ARTISTS))

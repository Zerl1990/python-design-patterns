import os
import pickle
import random
import string


class Memento:
    def __init__(self):
        self._f_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        self._f_name = os.path.join("./bk", self._f_name)

    @property
    def value(self):
        with open(self._f_name, "rb") as file:
            return pickle.load(file)

    @value.setter
    def value(self, instance: object):
        with open(self._f_name, "wb") as file:
            pickle.dump(instance, file)


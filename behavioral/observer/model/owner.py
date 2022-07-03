from behavioral.observer.model.model import Model
from behavioral.observer.observables.observable_field import ObservableField


class Owner(Model):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = ObservableField("First Name", str)
        self.last_name = ObservableField("Last Name", str)
        self.first_name.value = first_name
        self.last_name.value = last_name

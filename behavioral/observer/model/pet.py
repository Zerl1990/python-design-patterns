from behavioral.observer.model.model import Model
from behavioral.observer.model.owner import Owner
from behavioral.observer.observables.observable_field import ObservableField


class Pet(Model):
    def __init__(self, name: str, age: int, owner: Owner):
        self.name = ObservableField("Pet Name", str)
        self.age = ObservableField("Pet Age", int)
        self.owner = ObservableField("Pet Owner", Owner)
        self.name.value = name
        self.age.value = age
        self.owner.value = owner

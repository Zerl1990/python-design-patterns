from behavioral.observer.model.owner import Owner
from behavioral.observer.model.pet import Pet
from behavioral.observer.observers.field_console_observer import ConsoleObserver

if __name__ == "__main__":
    console_observer = ConsoleObserver()
    owner = Owner(first_name="Luis", last_name="Rivas")
    owner.add_observer(console_observer)
    pet = Pet(name="Luna", age=5, owner=owner)
    pet.add_observer(console_observer)

    owner.last_name.value = "Zepeda"
    pet.age.value = 6
    pet.name.value = "lun@"

    owner.remove_observer(console_observer)
    pet.remove_observer(console_observer)
    owner.last_name.value = "Rivas"
    pet.age.value = 10
    pet.name.value = "Luna"

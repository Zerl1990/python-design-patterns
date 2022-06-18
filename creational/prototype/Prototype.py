import copy


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier: str, obj: object):
        self.objects[identifier] = obj

    def unregister(self, identifier: str):
        del self.objects[identifier]

    def clone(self, identifier, **kwargs) -> object:
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f"Incorrect object identifier: {identifier}")
        obj = copy.deepcopy(found)
        for attr, value in kwargs.items():
            setattr(obj, attr, value)
        return obj

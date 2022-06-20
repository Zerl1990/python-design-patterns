

class Adapter:
    def __init__(self, obj: object, adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.obj)




class ResourceContent:
    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)

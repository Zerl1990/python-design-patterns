from behavioral.chain_of_responsabilities.elements.element import Widget


class MainWindow(Widget):
    def __init__(self, name: str, parent: Widget = None):
        super().__init__(parent)
        self.name = name

    def handle_close(self, event):
        print(f"[CLOSE] {self.name}: {event}")

    def handle_default(self, event):
        print(f"[DEFAULT] {self.name}: {event}")

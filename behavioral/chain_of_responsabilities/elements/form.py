from behavioral.chain_of_responsabilities.elements.element import Widget


class Form(Widget):
    def __init__(self, name: str, parent: Widget = None):
        super().__init__(parent)
        self.name = name

    def handle_submit(self, event):
        print(f"[SUBMIT] {self.name}: {event}")

from behavioral.chain_of_responsabilities.elements.element import Widget


class TextBox(Widget):
    def __init__(self, name: str, parent: Widget = None):
        super().__init__(parent)
        self.name = name

    def handle_send_keys(self, event):
        print(f"[SEND KEYS] {self.name}: {event}")

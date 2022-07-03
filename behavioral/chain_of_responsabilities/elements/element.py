from behavioral.chain_of_responsabilities.events.event import Event


class Widget:
    _DEF_HANDLER = "handle_default"

    def __init__(self, parent):
        self.parent = parent

    def handle(self, event: Event):
        handler = f"handle_{event}"
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent is not None:
            self.parent.handle(event)
        elif hasattr(self, Widget._DEF_HANDLER):
            self.handle_default(event)

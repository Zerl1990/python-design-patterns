from behavioral.chain_of_responsabilities.events.event import Event
from behavioral.chain_of_responsabilities.elements.window import MainWindow
from behavioral.chain_of_responsabilities.elements.text_box import TextBox
from behavioral.chain_of_responsabilities.elements.form import Form

if __name__ == "__main__":
    main_window = MainWindow(name="MAIN WINDOW")
    form = Form(name="FORM", parent=main_window)
    text_box_1 = TextBox(name="TEXT BOX 1", parent=form)
    text_box_2 = TextBox(name="TEXT BOX 2", parent=form)

    for event_name in ("send_keys", "submit", "unhandled", "close"):
        event = Event(event_name)
        for widget in (main_window, form, text_box_1, text_box_2):
            print(f"Send event -> {event} -> {widget.name}")
            widget.handle(event)

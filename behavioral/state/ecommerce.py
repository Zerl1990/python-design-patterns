from statemachine import StateMachine, State


class ECommerce(StateMachine):
    # State
    _start = State("Start", initial=True)
    _home = State("Home")
    _dummy = State("Dummy")

    # Event
    open = _start.to(_home)
    dummy_action = _home.to(_dummy)

    # Event Listeners
    def on_open(self):
        print("[AUTOMATION] - Open Web Page")

    def on_dummy_action(self):
        print("[AUTOMATION] - Dummy Action")

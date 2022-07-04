from statemachine import StateMachine, State


class TestRunner(StateMachine):
    _queue = State("Queue", initial=True)
    _init = State("Init")
    _running = State("Running")
    _skipped = State("Skipped")
    _failed = State("Failed")
    _passed = State("Passed")

    start = _queue.to(_init)
    run = _init.to(_running)
    ignored = _running.to(_skipped)
    failure = _running.to(_failed)
    success = _running.to(_passed)

    def on_start(self):
        print("Starting new test case")

    def on_run(self):
        print("Test case is running")

    def on_ignored(self):
        print("Test case will be ignored")

    def on_failure(self):
        print("Test case failed")

    def on_success(self):
        print("Test success")


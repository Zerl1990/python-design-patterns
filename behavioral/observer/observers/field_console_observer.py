from behavioral.observer.common.observer import Observer


class ConsoleObserver(Observer):
    def receive_observable_notification(self, *args, **kwargs):
        f_name = kwargs.get("name")
        f_value = kwargs.get("value")
        f_type = kwargs.get("type")
        print(f"[CONSOLE OBSERVER][{f_type}] {f_name} updated to {f_value}")

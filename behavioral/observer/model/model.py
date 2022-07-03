from behavioral.observer.observables.observable_field import ObservableField
from behavioral.observer.observers.field_console_observer import ConsoleObserver


class Model:
    def add_observer(self, observer: ConsoleObserver):
        for name, value in vars(self).items():
            if isinstance(value, ObservableField):
                value.subscribe(observer)

    def remove_observer(self, observer: ConsoleObserver):
        for name, value in vars(self).items():
            if isinstance(value, ObservableField):
                value.unsubscribe(observer)
from enum import auto, IntEnum


class Observable(object):

    def __init__(self):
        self._subscribers = list()

    def subscribe(self, observer):
        if observer not in self._subscribers:
            self._subscribers.append(observer)

    def notify_all(self, event, *args, **kwargs):
        for observer in self._subscribers:
            observer.notify(event, *args, **kwargs)


class Observer(object):

    def __init__(self, observables, callback):
        self._callback = callback
        for observable in observables:
            observable.subscribe(self)

    def notify(self, event, *args, **kwargs):
        self._callback(event, *args, **kwargs)


class Event(IntEnum):

    UPDATE = auto()
    COMPLETED = auto()


class InputCell(Observable):

    def __init__(self, initial_value):
        super().__init__()
        self.value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self.notify_all(Event.UPDATE)
        self.notify_all(Event.COMPLETED)


class ComputeCell(Observable, Observer):

    def __init__(self, inputs, compute_function):
        Observable.__init__(self)
        Observer.__init__(self, inputs, lambda event: self.dispatch_notification(event, inputs, compute_function))
        self.value = compute_function([i.value for i in inputs])
        self._prev_value = self.value
        self._callbacks = list()

    def dispatch_notification(self, event, inputs, compute_function):
        if event == Event.UPDATE:
            self.value = compute_function([i.value for i in inputs])
        elif event == Event.COMPLETED:
            if self.value != self._prev_value:
                self.notify_all(Event.UPDATE)
                self._prev_value = self.value
                for callback in self._callbacks:
                    callback(self.value)
            self.notify_all(Event.COMPLETED)

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)

class LogicGate:
    def __init__(self, entries) -> None:
        # TODO: add type checks for entries, avoid circular import somehow
        self._entries = entries

    def value(self):
        pass


class AndGate(LogicGate):
    pass

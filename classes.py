class FlipFlop:
    def __init__(self, id, entry, value) -> None:
        self.id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if not new_id:
            raise ValueError
        self._id = new_id


class LogicGate:
    def __init__(self, entries, type) -> None:
        pass

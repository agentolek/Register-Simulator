from logic_gate import LogicGate


class FlipFlop:
    # TODO: write nice looking doc string for flipflop class
    def __init__(self, id, entry, value) -> None:
        self._id = id

        # TODO: once done with rest of project, remove type checks here
        if not (
            isinstance(entry, FlipFlop)
            or isinstance(entry, LogicGate)
            or isinstance(entry, bool)
        ):
            raise ValueError

        self._entry = entry

        if not isinstance(value, bool):
            raise ValueError
        self._value = value

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, new_id) -> None:
        if not new_id:
            raise ValueError
        self._id = new_id

    @property
    def value(self) -> bool:
        """
        Whenever you get the value, the update_value method is called to make
        sure returned value is up to date.
        """
        return self._value

    def load_value(self, value) -> None:
        """
        Load value directly into flip-flop, regardless of values on input.
        """
        if not isinstance(value, bool):
            raise ValueError
        self._value = value

    def update_value(self) -> None:
        """
        Set the value of the flip-flop to be equal to the value of its entry.
        """
        if isinstance(self._entry, bool):
            self.load_value(self._entry)
        else:
            self.value = self._entry.value

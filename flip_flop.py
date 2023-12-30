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
        Get the current value of flip-flop.
        """
        return self._value

    def updated_value(self):
        return self._entry.value

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
            self._value = self._entry.value

    def set_entry(self, new_entry) -> None:
        """
        Used during creation of register to set it up. Changes initial entry
        from bool to LogicGate / previous FlipFlop.
        """
        self._entry = new_entry

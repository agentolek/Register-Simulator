class LogicGate:
    """
    Class LogicGate. Contains values:
    :param entries: The FlipFlops/LogicGates entering the LogicGate.
    :type entries: list[FlipFlop|LogicGate|bool]

    :param type: The type of logic gatde.
    :type type: str

    :param value: Returns the value of the LogicGate.
    :type value: bool
    """

    def __init__(self, entries: list, type_: str) -> None:
        self._entries = entries
        self._type = type_

    @property
    def value(self) -> bool:
        return self.AVAILABLE_TYPES.get(self._type)(self)

    def and_value(self) -> bool:
        """
        Entries - 1 to infinity.
        Returns True if all "subvalues" of LogicGate are True,
        otherwise returns False.
        """
        if sum(entry.value for entry in self._entries) == len(self._entries):
            return True
        else:
            return False

    def or_value(self) -> bool:
        """
        Entries - 1 to infinity.
        Returns True if at least one subvalue of LogicGate is True,
        returns False only if all subvalues are False.
        """
        if sum(entry.value for entry in self._entries) >= 1:
            return True
        else:
            return False

    def not_value(self) -> bool:
        """
        Entries - only 1.
        Returns the opposite value of entry.
        """
        return not self._entries[0].value

    def nand_value(self) -> bool:
        """
        Entries - 1 to infinity.
        Returns False if all "subvalues" of LogicGate are True,
        otherwise returns True. Opposite of AND.
        """
        return not self.and_value()

    def nor_value(self) -> bool:
        """
        Entries - 1 to infinity.
        Returns False if at least one subvalue of LogicGate is True,
        returns True only if all subvalues are False. Opposite of OR.
        """
        return not self.or_value()

    # dict of currently available types. Each type has its "value method"
    # given as value.
    AVAILABLE_TYPES = {
        "AND": and_value,
        "OR": or_value,
        "NOT": not_value,
        "NAND": nand_value,
        "NOR": nor_value,
    }

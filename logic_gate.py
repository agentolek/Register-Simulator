class NotAvailableTypeError(Exception):
    def __init__(self, type_) -> None:
        super().__init__(
            f"A LogicGate in input json uses unsupported type {type_}!",
        )


class EntryAmountError(Exception):
    pass


class LogicGate:
    """
    Class LogicGate. Contains values:
    :param entries: The FlipFlops/LogicGates entering the LogicGate.
    :type entries: list[FlipFlop|LogicGate|bool]

    :param type: The type of logic gate.
    :type type: str

    :param value: Returns the value of the LogicGate.
    :type value: bool
    """

    def __init__(self, entries, type_) -> None:
        if not entries:
            raise EntryAmountError(
                "No entries were given in a LogicGate in input json!"
            )
        self._entries = entries
        if type_.upper() not in self.AVAILABLE_TYPES:
            raise NotAvailableTypeError(type_)
        self._type = type_
        if self._type == "NOT" and len(entries) != 1:
            raise EntryAmountError(
                f"NOT gate accepts only one entry! Gate currently has {len(entries)} entries"
            )

    @property
    def value(self):
        return self.AVAILABLE_TYPES.get(self._type)(self)

    def and_value(self):
        """
        Entries - 1 to infinity.
        Returns True if all "subvalues" of LogicGate are True,
        otherwise returns False.
        """
        if sum(entry.value for entry in self._entries) == len(self._entries):
            return True
        else:
            return False

    def or_value(self):
        """
        Entries - 1 to infinity.
        Returns True if at least one subvalue of LogicGate is True,
        returns False only if all subvalues are False.
        """
        if sum(entry.value for entry in self._entries) >= 1:
            return True
        else:
            return False

    def not_value(self):
        """
        Entries - only 1.
        Returns the opposite value of entry.
        """
        return not self._entries[0].value

    def nand_value(self):
        """
        Entries - 1 to infinity.
        Returns False if all "subvalues" of LogicGate are True,
        otherwise returns True. Opposite of AND.
        """
        return not self.and_value()

    def nor_value(self):
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

class NotAvailableTypeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(
            "LogicGate type given is not supported!",
        )


class EntryAmountError(Exception):
    pass


class LogicGate:
    def __init__(self, entries, type) -> None:
        if not entries:
            raise EntryAmountError("No entries were given!")
        self._entries = entries
        if type.upper() not in self.AVAILABLE_TYPES:
            raise NotAvailableTypeError(entries)
        self._type = type
        if self._type == "NOT" and len(entries) != 1:
            raise EntryAmountError("NOT gate accepts only one entry!", entries)

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

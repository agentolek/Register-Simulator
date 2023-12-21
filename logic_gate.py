class NotAvailableTypeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("LogicGate type given is not supported!")


class EntryAmountError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(
            "The number of submitted entries is not supported by selected type."
        )


class LogicGate:
    """
    List of currently available types.
    """

    AVAILABLE_TYPES = ["AND", "OR", "NOT"]

    def __init__(self, entries, type) -> None:
        if not entries:
            raise EntryAmountError
        self._entries = entries
        if type.upper() not in self.AVAILABLE_TYPES:
            raise NotAvailableTypeError
        self._type = type
        try:
            self.value
        except EntryAmountError:
            raise EntryAmountError

    @property
    def value(self):
        match self._type:
            case "AND":
                return self.and_value()
            case "OR":
                return self.or_value()
            case "NOT":
                return
            # add value funcs for new LogicGate types here.
            case _:
                raise NotAvailableTypeError

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
        '''
        Entries - only 1.
        '''
        if len(self._entries) != 1:


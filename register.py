class Register:
    def __init__(self, flip_flops) -> None:
        self._flip_flops = flip_flops

    def __len__(self):
        return len(self._flip_flops)

    def values(self):
        """
        Returns a list of bools, which contain the current values of
        FlipFlops in register.
        """
        return [flip_flop.value for flip_flop in self._flip_flops]

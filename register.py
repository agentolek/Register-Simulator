class Register:
    """
    Class Register. Contains values:
    :param flip_flops: List of flip_flops in register.
    :type flip_flops: List[FlipFlop]
    """

    def __init__(self, flip_flops) -> None:
        self.flip_flops = flip_flops

    def __len__(self):
        return len(self.flip_flops)

    def values(self):
        """
        Returns a list of bools, which contain the current values of
        FlipFlops in register.
        """
        return [flip_flop.value for flip_flop in self.flip_flops]

    def updated_values(self):
        """
        Returns the values of entries of each register.
        """
        return [flip_flop.updated_value() for flip_flop in self.flip_flops]

    def value_of_index(self, index):
        """
        Returns the value of a single flip-flop in register.
        """
        return self.flip_flops[index]

    def update(self):
        """
        Updates the values in register to match the current values on entries.
        """
        new_values = self.updated_values()
        for i in range(len(new_values)):
            self.flip_flops[i].load_value(new_values[i])

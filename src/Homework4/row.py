class ROW:
    """
    Stores one record.
    """

    def __init__(self, t):
        """
        Constructor.

        Args:
            t (list): Data to add to the ROW.
        """

        self.cells = t

    def __repr__(self):
        return "a: {} cells: {}".format(self.__class__.__name__, self.cells)

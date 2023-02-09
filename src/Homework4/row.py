class ROW:
    """
    Store one record
    """
    def __init__(self, t):
        """
        Constructor

        Args:
            t (list): data to add to the cells of the row
        """
        self.cells = t

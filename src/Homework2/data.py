import cols
import row
import utils


class DATA:
    """
    Stores rows, summarized into columns.
    """

    def __init__(self, src=[]):
        """
        Constructor.

        Args:
            src (str/list, optional): Filename or list of data that DATA will be populated with. Defaults to [].
        """

        self.rows = []
        self.cols = None

        if type(src) == str:
            utils.csv(src, self.add)
        else:
            for v in src:
                self.add(v)

    def add(self, t):
        """
        Adds a new row and updates column headers.

        Args:
            t (list): Data that will either be added to a row or the column headers.
        """

        if self.cols:
            if not hasattr(t, "cells"):
                t = row.ROW(t)

            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = cols.COLS(t)

    def clone(self, init=[]):
        """
        Returns a DATA with the same structure.

        Args:
            init (list, optional): Rows of the DATA to be cloned. Defaults to [].

        Returns:
            DATA: Cloned DATA.
        """

        data = DATA([self.cols.names])

        for v in init:
            data.add(v)

        return data

    def stats(self, what, cols, nPlaces):
        """
        Reports the mid or div of the columns.

        Args:
            what (str): Either "mid" or "div". Defaults to "mid".
            cols (list): Columns that the stats are being taken from. Defaults to DATA.cols.y.
            nPlaces (int): Number of places to round the stats to.
        """

        def fun(col):
            return round(getattr(col, what or "mid")(), nPlaces), col.txt

        return {k[1]: k[0] for k in sorted(list(map(fun, cols or self.cols.y)), key=lambda tuple: tuple[1])}

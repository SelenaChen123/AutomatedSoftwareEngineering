import cols
import row
import utils


class DATA:
    """
    Store many rows, summarized into columns
    """
    def __init__(self, src):
        """
        A container of `i.rows`, to be summarized in `i.cols`

        Args:
            src (string/list): the filename or list of data that the data object will be populated by
        """
        self.rows = []
        self.cols = None

        if type(src) == str:
            utils.csv(src, self.add)
        else:
            utils.map(src or [], self.add)

    def add(self, t):
        """
        Add a new row, update column headers

        Args:
            t (list): the daat that will either be added to a row or to the column headers
        """
        if self.cols:
            if not hasattr(t, "cells"):
                t = row.ROW(t)

            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = cols.COLS(t)

    def clone(self, init):
        """
        Return a Data object with the same structure

        Args:
            init (Data): the original Data object

        Returns:
            Data: the cloned data object
        """
        data = DATA([self.cols.names])
        utils.map(init or [], data.add)

        return data

    def stats(self, what, cols, nPlaces):
        """
        Reports mid or div of the columns (defaults to i.cols.y)

        Args:
            what (string): the function to be done, either mid or div
            cols (list): the columns that stats are being taken from
            nPlaces (int): number of places to round the stat to
        """
        def fun(col):
            return round(getattr(col, what or "mid")(), nPlaces), col.txt

        mapped = utils.map(cols or self.cols.y, fun)
        return {k: mapped[k] for k in sorted(mapped.keys())}

import cols
import globals
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

    def dist(self, row1, row2, cols=None):
        """
        Returns the distance from row1 to row2.

        Args:
            row1 (ROW): First ROW to calculate the distance from.
            row2 (ROW): Second ROW to calculate the distance from.
            cols (COLS, optional): Factory that manages the locations of the rows. Defaults to DATA.cols.x.

        Returns:
            float: Distance from row1 to row2.
        """

        n = 0
        d = 0

        for col in cols or self.cols.x:
            n += 1
            d += col.dist(row1.cells[col.at],
                          row2.cells[col.at]) ** globals.the["p"]

        return (d / n) ** (1 / globals.the["p"])

    def around(self, row1, rows=[], cols=None):
        """
        Sorts rows by their distance to row1.

        Args:
            row1 (ROW): ROW to calculate the distance of the other ROWs from.
            rows (list, optional): List of ROWs to be sorted. Defaults to DATA.rows.
            cols (COLS, optional): Factory that manages rows. Defaults to None.
        """

        def function(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        return sorted(map(function, rows or self.rows), key=lambda d: d["dist"])

    def furthest(self, row1, rows, cols=None, t=[]):
        """
        Sorts other rows by tjheir distance to row1.

        Args:
            row1 (_type_): _description_
            rows (_type_): _description_
            cols (_type_): _description_
            t (_type_): _description_

        Returns:
            _type_: _description_
        """

        t = self.around(row1, rows, cols)

        return t[len(t) - 1]

    def half(self, rows=[], cols=None, above=None):
        """
        Divides DATA using 2 far points.

        Args:
            rows (list, optional): List of ROWs to be halved. Defaults to DATA.rows.
            cols (COLS, optional): Factory that manages rows. Defaults to None.
            above (ROW, optional): Single chosen ROW. Defaults to None.

        Returns:
            list: Left half of the ROWs.
            list: Right half of the ROWs.
            ROW: Single chosen ROW to calculate the distance from.
            ROW: Single chosen ROW around A to calculate the distance from.
            ROW: Middle ROW of the ROWs.
            float: Distance from A to B.
        """

        def project(row):
            x, y = utils.cosine(self.dist(row, A, cols),
                                self.dist(row, B, cols), c)

            if not hasattr(row, "x"):
                row.x = x
            if not hasattr(row, "y"):
                row.y = y

            return {"row": row, "x": x, "y": y}

        A = above or utils.any(rows or self.rows)
        B = self.furthest(A, rows or self.rows)["row"]
        c = self.dist(A, B, cols)
        left = []
        right = []

        for n, tmp in enumerate(sorted(map(project, rows or self.rows), key=lambda d: d["x"])):
            if n < len(rows or self.rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])

        return left, right, A, B, mid, c

    def cluster(self, rows=[], cols=None, above=[]):
        """
        Recursively halves rows.

        Args:
            rows (list, optional): List of ROWs to be halved. Defaults to DATA.rows.
            cols (COLS, optional): Factory that manages rows. Defaults to DATA.cols.x.
            above (ROW, optional): Single chosen ROW. Defaults to [].

        Returns:
            dict: Dictionary of remaining DATA to be recursively halved.
        """

        node = {"data": self.clone(rows or self.rows)}

        if len(rows or self.rows) >= 2:
            left, right, node["A"], node["B"], _, node["c"] = self.half(
                rows or self.rows, cols or self.cols.x, above)

            node["left"] = self.cluster(left, cols or self.cols.x, node["A"])
            node["right"] = self.cluster(right, cols or self.cols.x, node["B"])

        return node

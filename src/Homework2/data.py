import cols
import row
import utils


class DATA:

    def __init__(self, src):
        self.rows = []
        self.cols = None

        if type(src) == str:
            utils.csv(src, self.add)
        else:
            utils.map(src or [], self.add)

    def add(self, t):
        if self.cols:
            if not hasattr(t, "cells"):
                t = row.ROW(t)

            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = cols.COLS(t)

    def clone(self, init):
        data = DATA([self.cols.names])
        utils.map(init or [], data.add)

        return data

    def stats(self, what, cols, nPlaces):
        def fun(col):
            return round(getattr(col, what or "mid")(), nPlaces), col.txt

        mapped = utils.map(cols or self.cols.y, fun)
        return {k: mapped[k] for k in sorted(mapped.keys())}

from cols import COLS
from row import ROW
from utils import csv, map, kap


class DATA:

    def __init__(self, src):
        self.rows = []
        self.cols = None

        if type(src) == "string":
            csv(src, self.add())
        else:
            if type(src) == list:
                m = map(src, self.add)
            else:
                m = map({}, self.add)

    def add(self, t):
        if self.cols:
            if not t.cells:
                t = ROW(t)

            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)

    def clone(self, init):
        data = DATA([self.cols.names])

        if type(init) == list:
            map(init, data.add)
        else:
            map([], data.add)

        return data

    def stats(self, what, cols, func):
        if what == "mid":
            func = getattr(globals()["SYM"](), ("mid"))
        else:
            func = getattr(globals()["SYM"](), ("div"))

        if type(cols) == "COLS":
            return kap(cols, func)
        else:
            return kap(self.cols.y, func)

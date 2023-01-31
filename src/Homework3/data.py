import cols
import row
import utils
from functools import cmp_to_key

import globals


class DATA:

    def __init__(self, src):
        self.rows = []
        self.cols = None

        if type(src) == str:
            utils.csv(src, self.add)
        else:
            map(src or [], self.add)

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
        map(init or [], data.add)

        return data

    def stats(self, what, cols, nPlaces):
        def fun(col):
            return round(getattr(col, what or "mid")(), nPlaces), col.txt

        mapped = utils.map(cols or self.cols.y, fun)
        return {k: mapped[k] for k in sorted(mapped.keys())}

    def dist(self, row1, row2, cols, n, d):
        n = 0
        d = 0

        for _, col in enumerate(cols or self.cols.x):
            n += 1
            d += col.dist(row1.cells[col.at],
                          row2.cells[col.at]) ** globals.the["p"]

        return (d / n) ** (1 / globals.the["p"])

    def around(self, row1, rows, cols):
        def function(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        def lt(a, b):
            return a["dist"] < b["dist"]

        return sorted(map(rows or self.rows, function), key=cmp_to_key(lt))

    def cluster(self, rows, min, cols, above):
        node = {"data": self.clone(rows or self.rows)}

        if len(rows or self.rows) > 2 * (min or len(rows) ** globals.the["min"]):
            left, right, node.A, node.B, node.mid = self.half(
                rows, cols or self.cols.x, above)
            node.left = self.cluster(left, min or len(
                rows) ** globals.the["min"], cols or self.cols.x, node.A)
            node.right = self.cluster(right, min or len(
                rows) ** globals.the["min"], cols or self.cols.x, node.B)

        return node

    def sway(self, rows, min, cols, above):
        node = {"data": self.clone(rows or self.rows)}

        if len(rows or self.rows) > 2 * (min or len(rows) ** globals.the["min"]):
            left, right, node.A, node.B, node.mid = self.half(
                rows, cols or self.cols.x, above)

            if self.better(node.B, node.A):
                left, right, node.A, node.B = right, left, node.B, node.A

            node.left = self.sway(left, min or len(
                rows) ** globals.the["min"], cols or self.cols.x, node.A)

        return node

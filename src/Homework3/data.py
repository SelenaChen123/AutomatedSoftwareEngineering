from functools import cmp_to_key
import math

import globals
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
            for v in src or []:
                self.add(v)

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

        for v in init or []:
            data.add(v)

        return data

    def stats(self, what, cols, nPlaces):
        def fun(col):
            return round(getattr(col, what or "mid")(), nPlaces), col.txt

        return {k[1]: k[0] for k in sorted(list(map(fun, cols or self.cols.y)), key=lambda tuple: tuple[1])}

    def dist(self, row1, row2, cols=None):
        n = 0
        d = 0

        for col in cols or self.cols.x:
            n += 1
            d += col.dist(row1.cells[col.at],
                          row2.cells[col.at]) ** globals.the["p"]

        return (d / n) ** (1 / globals.the["p"])

    def around(self, row1, rows=[], cols=None):
        def function(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        return sorted(map(function, rows or self.rows), key=cmp_to_key(utils.lt))

    def better(self, row1, row2):
        s1 = 0
        s2 = 0
        ys = self.cols.y

        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 -= math.exp(col.w * (x - y) / len(ys))
            s2 -= math.exp(col.w * (y - x) / len(ys))

        return s1 / len(ys) < s2 / len(ys)

    def half(self, rows=[], cols=None, above=None):
        mid = None

        def project(row):
            return {"row": row, "dist": utils.cosine(self.dist(row, A, cols), self.dist(row, B, cols), c)}

        some = utils.many(rows or self.rows, globals.the["Sample"])
        A = above or utils.any(some)
        B = self.around(A, some)[math.floor(
            globals.the["Far"] * len(rows))]["row"]
        c = self.dist(A, B, cols)
        left = []
        right = []

        for n, tmp in enumerate(sorted(map(project, rows or self.rows), key=cmp_to_key(utils.lt))):
            if n < len(rows or self.rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])

        return left, right, A, B, mid, c

    def cluster(self, rows=[], min=0, cols=None, above=[]):
        node = {"data": self.clone(rows or self.rows)}

        if len(rows or self.rows) > 2 * (min or len(rows) ** globals.the["min"]):
            node["left"], node["right"], node["A"], node["B"], node["mid"], _ = self.half(
                rows, cols or self.cols.x, above)

            node["left"] = self.cluster(node["left"], min or len(
                rows) ** globals.the["min"],  cols or self.cols.x, node["mid"])
            node["right"] = self.cluster(node["right"], min or len(
                rows) ** globals.the["min"], cols or self.cols.x, node["B"])

        return node

    def sway(self, rows=[], min=0, cols=None, above=[]):
        node = {"data": self.clone(rows or self.rows)}

        if len(rows or self.rows) > 2 * (min or len(rows) ** globals.the["min"]):
            node["left"], node["right"], node["A"], node["B"], node["mid"], _ = self.half(
                rows, cols or self.cols.x, above)

            if self.better(node["B"], node["A"]):
                node["left"], node["right"], node["A"], node["B"] = node["right"], node["left"], node["B"], node["A"]

            node["left"] = self.sway(node["left"], min or len(
                rows) ** globals.the["min"], cols or self.cols.x, node["A"])

        return node

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

    
    def better(self, row1, row2):
         s1, s2, ys, x, y = 0, 0, self.cols.y, None, None
         for col in ys:
            
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - (col.w ** (x-y)/len(ys))
            s2 = s2 - (col.w ** (x-y)/len(ys)) 
         if s1/len(ys) < s2/len(ys):
            return True
         return False

    def half(self,row, cols, above):

        mid = None
        def cosine(a,b,c):
            x1 = (a**2 + b**2 + c**2)/(2*c)
            x2 = max(0, min(1, x1))
            y  = (a**2 - x2**2)**0.5
            return x2,y

        def project(row):
            return {"row":row, "dist":cosine(dist(row, A), dist(row, B), c)}

        def dist(row1, row2):
            return self.dist(row1, row2, cols)
        
        def lt(a, b):
            return a["dist"] < b["dist"]

        def many(t,n):
            u = {}
            for i in range(0,n):
                u[1+len(u)] = any(t)
            return u
        
        def any(t):
            return t[rint(len(t))]

        def rint(lo, hi):
            return (0.5 + rand(lo,hi))//1       

        def rand(lo,hi):
            Seed=937162211
            if lo == None:
                lo = 0
            if hi == None:
                hi = 1 
            Seed = (16807 * Seed) % 2147483647
            return lo + (hi-lo) * Seed / 2147483647

        rows = rows or self.rows
        some = many(rows, globals.the["sample"])

        A = above or any(above)
        B = self.around(A, some)[(globals.the["Far"] * len(rows))//1].row
        c = dist(A,B)

        left, right = [], []
        tmps = sorted(map(rows, project), key=cmp_to_key(lt))
        
        for n, tmp in tmps.items():
            if n < len(rows)//2:
                left.append(tmp.row)
                mid = tmp.row
            else:
                right.append(tmp.row)
        
        return left, right, A, B, mid, c
        
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

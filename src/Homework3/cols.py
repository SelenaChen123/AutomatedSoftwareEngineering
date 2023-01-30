import num
import sym

import re


class COLS:

    def __init__(self, t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = []

        for n, s in enumerate(t):
            if re.search("^[A-Z]+", s):
                col = num.NUM(n, s)
            else:
                col = sym.SYM(n, s)

            self.all.append(col)

            if not re.search("X$", s):
                if not re.search("!$", s):
                    self.klass = col

                if re.search("[!+-]$", s):
                    self.y.append(col)
                else:
                    self.x.append(col)

    def add(self, row):
        for col in self.x + self.y:
            col.add(row.cells[col.at])

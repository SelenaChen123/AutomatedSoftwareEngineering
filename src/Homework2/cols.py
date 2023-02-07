import num
import sym

import re


class COLS:
    """
    Factory for managing a set of NUMs or SYMs
    """
    def __init__(self, t):
        """
        Constructor: generate NUMs and SYMs from column names

        Args:
            t (list): the column of data
        """
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
        """
        Update the (not skipped) columns with details from "row"

        Args:
            row (Row): Row object to add data to the column from
        """
        for col in self.x + self.y:
            col.add(row.cells[col.at])

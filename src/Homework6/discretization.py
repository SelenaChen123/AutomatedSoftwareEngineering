import copy
import math

import creation
import globals
import query
import update


def bins(cols, rowss):
    """
    Returns RANGEs that map the rows in rowss to a small number of bins to reduce the search space.

    Args:
        cols (dict): Columns associated with the rows to be mapped to a small number of bins.
        rowss (dict): Rows to be mapped to a small number of bins.

    Returns:
        list: RANGES that map the rows in rowss to a small number of bins.
    """
    

    def with1Col(col):
        n, ranges = withAllRows(col)
        ranges = sorted(ranges.values(), key=lambda x: x["lo"])

        return ranges if "isSym" in col else merges(ranges, n / globals.Is["bins"], globals.Is["d"] * query.div(col))

    def withAllRows(col):
        def xy(x, y):
            if x != "?":
                global n
                n += 1
                k = bin(col, x)
                global ranges

                if k not in ranges:
                    ranges[k] = creation.RANGE(col["at"], col["txt"], x)

                update.extend(ranges[k], x, y)

        global n
        n = 0
        global ranges
        ranges = {}

        for y, rows in rowss.items():
            for row in rows:
                xy(row[col["at"]], y)

        return n, ranges

    return map(with1Col, cols)


def bin(col, x):
    """
    Maps a row to a small number of bins.

    Args:
        col (dict): Column associated with the row to be mapped to a small number of bins.
        x (dict): Row to be mapped to a small number of bins.

    Returns:
        float: Bin value that the row is mapped to.
    """
    

    if x == "?" or "isSym" in col:
        return x

    tmp = (col["hi"] - col["lo"]) / (globals.Is["bins"] - 1)

    return 1 if col["hi"] == col["lo"] else math.floor(x / tmp + 0.5) * tmp


def merges(ranges0, nSmall, nFar):
    

    def noGaps(t):
        for i in range(1, len(t)):
            t[i]["lo"] = t[i - 1]["hi"]

        t[0]["lo"] = -math.inf
        t[len(t) - 1]["hi"] = math.inf

        return t

    def try2Merge(left, right, i):
        y = merged(left["y"], right["y"], nSmall, nFar)

        if y:
            i += 1
            left["hi"] = right["hi"]
            left["y"] = y

        return i, left

    ranges1 = []
    i = 1

    while i <= len(ranges0):
        here = ranges0[i - 1]
        if i < len(ranges0):
            i, here = try2Merge(here, ranges0[i], i)
            i += 1
            ranges1.append(here)

    return noGaps(ranges0) if len(ranges0) == len(ranges1) else merges(ranges1, nSmall, nFar)


def merged(col1, col2, nSmall, nFar):
    
    new = merge(col1, col2)
    
    
    
    

    return new if nSmall and col1["n"] < nSmall or col2["n"] < nSmall or nFar and not "isSym" in col1 and abs(query.mid(col1) - query.mid(col2)) < nFar or query.div(new) <= (query.div(col1) * col1["n"] + query.div(col2) * col2["n"]) / new["n"] else None


def merge(col1, col2):
    
    """
    Merges col1 and col2.

    Args:
        col1 (dict): First column to be merged.
        col2 (dict): Second column to be merged.

    Returns:
        dict: Merged version of col1 and col2.
    """

    new = copy.deepcopy(col1)

    if "isSym" in col1:
        for x, n in col2["has"].items():
            update.add(new, x, n)
    else:
        for n in col2["has"].values():
            update.add(new, n)

        new["lo"] = min(col1["lo"], col2["lo"])
        new["hi"] = max(col1["hi"], col2["hi"])

    return new

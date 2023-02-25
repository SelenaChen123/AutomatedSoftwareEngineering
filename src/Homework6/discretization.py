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

    out = []

    for col in cols:
        ranges = {}

        for y, rows in rowss.items():
            for row in rows:
                x = row[col["at"]]

                if x != "?":
                    k = bin(col, x)

                    if k not in ranges:
                        ranges[k] = creation.RANGE(col["at"], col["txt"], x)

                    update.extend(ranges[k], x, y)

        ranges = sorted(ranges.values(), key=lambda x: x["lo"])
        out.append(ranges if "isSym" in col else mergeAny(ranges))

    return out


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

    tmp = (col["hi"] - col["lo"]) / (globals.the["bins"] - 1)

    return 1 if col["hi"] == col["lo"] else math.floor(x / tmp + 0.5) * tmp


def merges(ranges0, nSmall, nFar, noGaps, try2Merge):
    return "NOT YET IMPLEMENTED"


def merged(col1, col2, nSmall, nFar, new):
    return "NOT YET IMPLEMENTED"


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

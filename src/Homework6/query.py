import math

import globals
import utils


def has(col):
    """
    Returns the contents of col.

    Args:
        col (dict): Column to return the contents of.

    Returns:
        list: Contents of col.
    """

    if not "isSym" in col and not col["ok"]:
        col["has"].sort()

    col["ok"] = True

    return col["has"]


def mid(col):
    """
    Returns the central tendency of col.

    Args:
        col (dict): Column to get the central tendency of.

    Returns:
        float/str: Central tendency of col.
    """

    return col["mode"] if "isSym" in col else utils.per(has(col), .5)


def div(col):
    """
    Returns the deviation of col from its central tendency.

    Args:
        col (dict): Column to get the deviation from its central tendency.

    Returns:
        int/float/str: Deviation from its central tendency of col.
    """

    if "isSym" in col:
        e = 0

        for n in col["has"].values():
            e -= (n / col["n"]) * (math.log(n / col["n"], 2))

        return e
    else:
        return (utils.per(has(col), .9) - utils.per(has(col), .1)) / 2.58


def stats(data, fun=None, cols=None, nPlaces=2):
    """
    Reports the mid or div of cols.

    Args:
        data (dict, optional): Dictionary of data to report the mid or div of.
        fun (function, optional): Either mid() or div(). Defaults to mid().
        cols (list, optional): Columns that the stats are being taken from. Defaults to data["cols"["y"].
        nPlaces (int, optional): Number of places to round the stats to. Defaults to 2.

    Returns:
        dict: Report of the mid or div of cols.
    """

    cols = cols or data["cols"]["y"]

    def function(col):
        return col["txt"], round((fun or mid)(col), nPlaces)

    temp = dict(map(function, cols))
    temp["N"] = len(data["rows"])

    return dict(sorted(temp.items()))


def norm(num, n):
    """
    Normalizes n.

    Args:
        num (dict): Dictionary of data to get the lo and hi values used for normalization from.
        n (int/float): Number to be normalized.

    Returns:
        float: Normalized version of n.
    """

    return n if n == "?" else (n - num["lo"]) / (num["hi"] - num["lo"] + 1 / math.inf)


def value(has, nB, nR, sGoal=True):
    """
    Returns the score of a distribution of symbols.

    Args:
        has (dict): Dictionary of symbols to return the score of.
        nB (int): Size of the best.
        nR (int): Size of the rest.
        sGoal (bool, optional): Either "best" or "rest". Defaults to True.

    Returns:
        float: Score of the distribution of symbols.
    """

    b = 0
    r = 0

    for x, n in has.items():
        if x == sGoal:
            b += n
        else:
            r += n

    b = b / (nB + 1 / math.inf)
    r = r / (nR + 1 / math.inf)

    return b ** 2 / (b + r)


def dist(data, t1, t2, cols={}):
    """
    Returns the distance between t1 and t2.

    Args:
        data (dict): Dictionary of data to be used to calculate the distance between t1 and t2.
        t1 (list): First row to calculate the distance from.
        t2 (list): Second row to calculate the distance from.
        cols (dict, optional): Columns associated with the rows to calculate the distance between. Defaults to data["cols"]["x"].

    Returns:
        float: Distance between t1 and t2.
    """

    def dist1(col, x, y):
        if x == "?" and y == "?":
            return 1
        elif "isSym" in col:
            return 0 if x == y else 1
        else:
            x = norm(col, x)
            y = norm(col, y)

            if x == "?":
                x = 1
            if y == "?":
                y = 1

            return abs(x - y)

    d = 0
    n = 1 / math.inf

    for col in cols or data["cols"]["x"]:
        n += 1
        d += dist1(col, t1[col["at"]], t2[col["at"]]) ** globals.the["p"]

    return (d / n) ** (1 / globals.the["p"])


def better(data, row1, row2):
    """
    Checks whether or not row1 dominates row2.

    Args:
        data (dict): Dictionary of data to be used to check whether or not row1 dominates row2.
        row1 (list): Row to check if it dominates the second row.
        row2 (_type_): Row to check if it is dominated by the first row.

    Returns:
        bool: True if s1 divided by the length of ys < s2 divided by the length of ys, False otherwise.
    """

    s1 = 0
    s2 = 0
    ys = data["cols"]["y"]

    for col in ys:
        x = norm(col, row1[col["at"]])
        y = norm(col, row2[col["at"]])
        s1 -= math.exp(col["w"] * (x - y) / len(ys))
        s2 -= math.exp(col["w"] * (y - x) / len(ys))

    return s1 / len(ys) < s2 / len(ys)


def betters(data, n):
    return "NOT YET IMPLEMENTED"

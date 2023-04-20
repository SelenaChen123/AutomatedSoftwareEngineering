from functools import cmp_to_key
import math
import numpy as np
from deap import algorithms, base, creator, tools

# from pygmo import hypervolume

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


def stats(data, fun=None, cols=[], nPlaces=2):
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
    if n =="?":
        return n
    # print(n, num["lo"])
    if n - num["lo"]==0:
        return 0.00000000000000000000000000000000000000000000000000000000000000001/(num["hi"] - num["lo"] + 0.00000000000000000000000000000000000000000000000000000000000001)
    return (n - num["lo"]) / (num["hi"] - num["lo"] + 1 / math.inf)


def value(has, nB=1, nR=1, sGoal=True):
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

    def sym(x, y):
        return 0 if x == y else 1

    def num(x, y):
        if x == "?":
            x = 1

        if y == "?":
            y = 1

        return abs(x - y)

    def dist1(col, x, y):
        if x == "?" and y == "?":
            return 1
        elif "isSym" in col:
            return sym(x, y)
        else:

            return num(norm(col, x), norm(col, y))

    d = 0
    n = 1 / math.inf
    for col in cols or data["cols"]["x"]:
        n += 1
        d += dist1(col, t1[col["at"]], t2[col["at"]]) ** globals.Is["p"]
    return (d / n) ** (1 / globals.Is["p"])



def better(data, row1, row2):
    """
    Checks whether or not row1 dominates row2.
    Args:
        data (dict): Dictionary of data to be used to check whether or not row1 dominates row2.
        row1 (list): Row to check if it dominates the second row.
        row2 (list): Row to check if it is dominated by the first row.
    Returns:
        bool: True if row1 dominates row2, False otherwise.
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
    """
    Returns the best n items from data.

    Args:
        data (dict): Dictionary of data to return the best n items from.
        n (int): Number of items to return from data.

    Returns:
        list: List of the best n items from data.
    """

    def function(r1, r2):
        return -better(data, r1, r2)

    tmp = sorted(data["rows"], key=cmp_to_key(function))

    return tmp[1:n], tmp[n + 1:] if n else tmp


def better2(data, row1, row2):
    """
    Checks whether or not row1 dominates row2.
    Args:
        data (dict): Dictionary of data to be used to check whether or not row1 dominates row2.
        row1 (list): Row to check if it dominates the second row.
        row2 (list): Row to check if it is dominated by the first row.
    Returns:
        bool: True if row1 dominates row2, False otherwise.
    """

    # ys = data["cols"]["y"]
    # d1 = sum([norm(col, row1[col["at"]]) ** 2 for col in ys])
    # d2 = sum([norm(col, row2[col["at"]]) ** 2 for col in ys])
    # s1 = sum([norm(col, row1[col["at"]]) / math.sqrt(d1) * col["w"] for col in ys])
    # s2 = sum([norm(col, row2[col["at"]]) / math.sqrt(d2) * col["w"] for col in ys])
    # return s1/len(ys) > s2/len(ys)

    ys = data["cols"]["y"]
    d1 = sum([norm(col, row1[col["at"]]) ** 2 for col in ys])
    d2 = sum([norm(col, row2[col["at"]]) ** 2 for col in ys])
    if d1 == 0 or d2 == 0:
        return False
    else:
        s1 = 0
        s2 = 0
        for col in ys:
            x = norm(col, row1[col["at"]])
            y = norm(col, row2[col["at"]])
            if x > y:
                s1 += col["w"]
            elif y > x:
                s2 += col["w"]
        return s1/math.sqrt(d1) > s2/math.sqrt(d2)


    
    # Check if row1 dominates row2 or not
    if s1 == s2:
        return False
    else:
        return s1 > s2

def betters2(data, n):
    """
    Returns the best n items from data.

    Args:
        data (dict): Dictionary of data to return the best n items from.
        n (int): Number of items to return from data.

    Returns:
        list: List of the best n items from data.
    """

    def function(r1, r2):
        return -better2(data, r1, r2)

    tmp = sorted(data["rows"], key=cmp_to_key(function))

    return tmp[1:n], tmp[n + 1:] if n else tmp

def mid1(t):
    t = t["has"] if t["has"] else t

    return (t[(len(t) - 1) // 2] + t[(len(t) - 1) // 2 + 1]) / 2 if len(t) % 2 == 0 else t[(len(t) - 1) // 2 + 1]

def div1(t):

    t = t["has"] if "has" in t else t

    return (t[len(t) * 9 // 10] - t[len(t) * 1 // 10]) / 2.56

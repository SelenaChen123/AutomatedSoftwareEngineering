import math
import re


seed = 937162211


def coerce(s):
    if s == "true":
        return True
    elif s == "false":
        return False

    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s.strip()


def csv(sFilename, fun):
    with open(sFilename) as src:
        lines = src.readlines()

        for s in lines:
            t = []

            for s1 in re.findall("([^,]+)", s):
                t.append(coerce(s1))

            fun(t)


def lt(a, b):
    return a["dist"] < b["dist"]


def cosine(a, b, c):
    x1 = (a ** 2 + c ** 2 - b ** 2)

    if c != 0:
        x1 = x1 / (2 * c)

    x2 = max(0, min(1, x1))
    y = abs(a ** 2 - x2 ** 2) ** 0.5

    return x2, y


def rand(lo=0, hi=1):
    global seed
    seed = (16807 * seed) % 2147483647

    return lo + (hi - lo) * seed / 2147483647


def rint(lo=0, hi=1):
    return math.floor(0.5 + rand(lo, hi))


def many(t, n):
    return [any(t) for _ in range(0, n)]


def any(t):
    # return t[rint(0, len(t) - 1)]
    return t[rint(len(t)) - 1]


def show(node, what, cols, nPlaces, lvl=0):
    if "data" in node:
        print("{} {}  ".format("| " * lvl, len(node["data"].rows)), end="")

        print(node["data"].stats("mid", node["data"].cols.y, nPlaces)
              if "left" not in node or lvl == 0 else "")

        if "left" in node:
            show(node["left"], what, cols, nPlaces, lvl + 1)

        if "right" in node:
            show(node["right"], what, cols, nPlaces, lvl + 1)

def transpose(t):
    return 0

def repCols(cols):
    return 0

def repRows(t, rows):
    return 0

def repPlace(data, n = 20, g = {}, maxy = 0):
    return 0

def repgrid(file):
    return 0
import math

import utils


def has(col):
    if not col.get("isSym") and not col["ok"]:
        col["has"].sort()

    col["ok"] = True

    return col["has"]


def mid(col):
    return col["mode"] if col.get("isSym") else utils.per(has(col), .5)


def div(col):
    if col.get("isSym"):
        e = 0

        for n in col["has"]:
            e -= (n / col["n"]) * (math.log(n / col["n"], 2))

        return e

    return (utils.per(has(col), .9) - utils.per(has(col), .1)) / 2.58


def stats(data, fun, cols, nPlaces):
    cols = cols or data["cols"]["y"]

    def function(col):
        return round((fun or mid)(col), nPlaces), col["txt"]

    temp = map(function, cols)
    temp["N"] = len(data.rows)

    return temp


def norm(num, n):
    return n if n == "?" else (n - num["lo"]) / (num["hi"] - num["lo"] + 1 / math.inf)


def value(has, nB, nR):
    b, r = 0, 0

    for x, n in enumerate(has):
        if x:
            b += n
        else:
            r += n

    b = b / ((nB + 1) / math.inf)
    r = r / ((nR + 1) / math.inf)

    return b ** 2 / (b + r)


def dist(data, t1, t2, cols):
    def dist1(col, x, y):
        if x == "?" and y == "?":
            return 1
        elif col["isSym"]:
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
    s1 = 0
    s2 = 0
    ys = data["cols"]["y"]

    for col in ys:
        x = norm(col, row1[col["at"]])
        y = norm(col, row2[col["at"]])
        s1 -= math.exp(col["w"] * (x - y) / len(ys))
        s2 -= math.exp(col["w"] * (y - x) / len(ys))

    return s1 / len(ys) < s2 / len(ys)

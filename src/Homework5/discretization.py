import math
import copy
import creation
import query
import update
import globals


def bins(cols, rowss):
    out = []
    for col in cols:
        ranges = {}
        for y, rows in enumerate(rowss):
            for row in rows:
                x = row[col.at]
                if x != "?":
                    k = bin(col, x)
                    ranges[k] = ranges[k] or creation.RANGE(col.at, col.txt, x)
                    update.extend(ranges[k], x, y)

        ranges = sorted(list(ranges), key=lambda x: x["lo"])
        out.append(col.isSym and ranges or mergeAny(ranges))
    return out


def bin(col, x):
    if x == "?" or col["isSym"]:
        return x
    tmp = (col["hi"] - col["lo"])/(globals.the['bins'] - 1)
    if col["hi"] == col["lo"]:
        return 1
    return math.floor(x / tmp+0.5)*tmp


def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1, len(t) + 1):  # Lua indices start from 1
            t[j]["lo"] = t[j-1]["hi"]
        t[0]["lo"], t[len(t)-1]["hi"] = -math.inf, math.inf
        return t

    ranges1, j = [], 0

    while j < len(ranges0):
        left, right = ranges0[j], ranges0[j+1]
        if right:
            y = merge2(left["y"], right["y"])
            if y:
                j += 1
                left["hi"], left["y"] = right["hi"], y
        ranges1.append(left)
        j += 1

    if len(ranges0) == len(ranges1):
        return noGaps(ranges0)
    else:
        return mergeAny(ranges1)

def merge2(col1, col2):
    new = merge(col1, col2)
    if query.div(new) <= (query.div(col1)*col1["n"])/new["n"]:
        return new
    return None

def merge(col1, col2):
    new = copy.deepcopy(col1)
    if col1["isSym"]:
        for x, n in col2["has"].items():
            update.add(new, x, n)
    else:
        for n in col2["has"].values():
            update.add(new, n)
    new["lo"] = min(col1["lo"], col2["lo"])
    new["hi"] = max(col1.hi, col2.hi)
    return new
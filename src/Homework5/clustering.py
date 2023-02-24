import math

import globals
import creation
import utils
import query


def half(data, rows=[], cols=None, above=None):
    left, right = [], []

    def cos(a, b, c):
        return (a ** 2 + c ** 2 - b ** 2) / (2 * c)

    def proj(r):
        return {"row": r, "x": cos(query.dist(data, r, A, cols), query.dist(data, r, B, cols), c)}

    rows = rows or data["rows"]
    some = utils.many(rows, globals.the["Halves"])
    A = above if (globals.the["Reuse"] and above) else utils.any(some)
    tmp = sorted(
        list(map(lambda r: {"row": r, "d": query.dist(data, r, A, cols)}, some)), key=lambda x: x["d"])
    far = tmp[math.floor(len(tmp) * globals.the["Far"])]
    B = far["row"]
    c = far["d"]

    for n, two in enumerate(sorted(list(map(proj, rows)), key=lambda x: x["x"])):
        left.append(two["row"]) if n <= len(rows) / \
            2 else right.append(two["row"])

    return left, right, A, B, c


def tree(data, rows=[], cols=None, above=None):
    rows = rows or data["rows"]
    here = {"data": creation.clone(data, rows)}
    if len(rows) >= 2 * len(data["rows"]) ** globals.the["min"]:
        left, right, A, B, _ = half(data, rows, cols, above)
        here["left"] = tree(data, left, cols, A)
        here["right"] = tree(data, right, cols, B)

    return here


def showTree(tree, lvl=0):
    if tree:
        print("{}[{}] ".format("|.. " * lvl, len(tree["data"]["rows"])), end="")
        print((lvl == 0 or "left" in tree) and
              query.stats(tree["data"]) or "")

        if "left" in tree:
            showTree(tree["left"], lvl + 1)

        if "right" in tree:
            showTree(tree["right"], lvl + 1)

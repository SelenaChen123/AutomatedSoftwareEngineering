import math

import creation
import globals
import query
import utils


def half(data, rows=[], cols=None, above=[]):
    """
    Divides data using 2 far points.

    Args:
        data (dict): Data to be halved.
        rows (list, optional): List of rows to be halved. Defaults to data["rows"].
        cols (dict, optional): Factory that manages rows. Defaults to None.
        above (list, optional): Single chosen row. Defaults to [].

    Returns:
        list: Left half of the rows.
        list: Right half of the rows.
        list: Single chosen row to calculate the distance from.
        row: Single chosen row around A to calculate the distance from.
        float: Distance from A to B.
    """

    left = []
    right = []

    def cos(a, b, c):
        return (a ** 2 + c ** 2 - b ** 2) / (2 * c)

    def proj(r):
        return {"row": r, "x": cos(query.dist(data, r, A, cols), query.dist(data, r, B, cols), c)}

    rows = rows or data["rows"]
    some = utils.many(rows, globals.Is["Halves"])
    A = above if (globals.Is["Reuse"] and above) else utils.any(some)
    tmp = sorted(list(map(lambda r: {"row": r, "d": query.dist(
        data, r, A, cols)}, some)), key=lambda x: x["d"])
    far = tmp[math.floor((len(tmp) - 1) * globals.Is["Far"])]
    B = far["row"]
    c = far["d"]

    for n, two in enumerate(sorted(map(proj, rows), key=lambda x: x["x"])):
        left.append(two["row"]) if n <= len(rows) / \
            2 - 1 else right.append(two["row"])

    return left, right, A, B, c, (1 if (globals.Is["Reuse"] and above) else 2)


def tree(data, rows=[], cols=None, above=[], here={}):
    """
    Recursively halves rows.

    Args:
        data (dict): Data to be halved.
        rows (list, optional): List of rows to be halved. Defaults to data["rows"].
        cols (dict, optional): Factory that manages rows. Defaults to data["cols"]["x"].
        above (list, optional): Single chosen row. Defaults to [].

    Returns:
        dict: Dictionary of remaining data to be recursively halved.
    """

    rows = rows or data["rows"]
    here = {"data": creation.clone(data, rows)}

    if len(rows) >= 2 * len(data["rows"]) ** globals.Is["min"]:
        left, right, A, B, _, _ = half(data, rows, cols, above)
        here["left"] = tree(data, left, cols, A)
        here["right"] = tree(data, right, cols, B)

    return here


def showTree(tree, lvl=0):
    """
    Prints the tree version of the data.

    Args:
        tree (dict): Tree of data to be printed.
        lvl (int, optional): Current tree level. Defaults to 0.
    """

    if tree:
        print("{}[{}] ".format("|.. " * lvl, len(tree["data"]["rows"])), end="")
        print(query.stats(tree["data"]) if (
            lvl == 0 or "left" not in tree) else "")

        if "left" in tree:
            showTree(tree["left"], lvl + 1)

        if "right" in tree:
            showTree(tree["right"], lvl + 1)

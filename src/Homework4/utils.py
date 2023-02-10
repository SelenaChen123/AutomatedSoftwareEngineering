import copy
import json
import math
import re

import data


seed = 937162211


def coerce(s):
    """
    Coerces a str s into an int, float, bool, or trimmed str.

    Args:
        s (str): Str to be coerced into an int, float, bool, or trimmed str.

    Returns:
        int/float/bool/str: int, float, bool, or trimmed str version of s.
    """

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
    """
    Calls the function fun on the rows after coercing the cell text.

    Args:
        sFilename (str): Filename of the csv file.
        fun (function): Function to be performed on each row of the csv file.
    """

    with open(sFilename) as src:
        lines = src.readlines()

        for s in lines:
            t = []

            for s1 in re.findall("([^,]+)", s):
                t.append(coerce(s1))

            fun(t)


def cosine(a, b, c):
    """
    Finds x and y from the line connecting a to b.

    Args:
        a (float): a value to calculate the cosine from.
        b (float): b value to calculate the cosine from.
        c (float): c value to calculate the cosine from.

    Returns:
        int/float: x from the line connecting a to b.
        float: y from the line connecting a to b.
    """

    x1 = (a ** 2 + c ** 2 - b ** 2)

    if c != 0:
        x1 = x1 / (2 * c)

    x2 = max(0, min(1, x1))
    y = abs(a ** 2 - x2 ** 2) ** 0.5

    return x2, y


def rand(lo=0, hi=1):
    """
    Generates a random float between lo (inclusive) and hi (not inclusive).

    Args:
        lo (int, optional): Lower bound for the random float generation. Defaults to 0.
        hi (int, optional): Upper bound for the random float generation. Defaults to 1.

    Returns:
        float: Random float between lo (inclusive) and hi (not inclusive).
    """

    global seed
    seed = (16807 * seed) % 2147483647

    return lo + (hi - lo) * seed / 2147483647


def rint(lo=0, hi=1):
    """
    Generates a random int between lo (inclusive) and hi (not inclusive).

    Args:
        lo (int, optional): Lower bound for the random int generation. Defaults to 0.
        hi (int, optional): Upper bound for the random int generation. Defaults to 1.

    Returns:
        int: Random int between lo (inclusive) and hi (not inclusive).
    """

    return math.floor(0.5 + rand(lo, hi))


def many(t, n):
    """
    Returns n ROWs from t.

    Args:
        t (list): List to return the ROWs from.
        n (int): Number of ROWs to be returned.

    Returns:
        list: List of n ROWs from t.
    """

    return [any(t) for _ in range(0, n)]


def any(t):
    """
    Returns a random ROW from t.

    Args:
        t (list): List to return the random ROW from.

    Returns:
        ROW: Random row from t.
    """

    # return t[rint(0, len(t) - 1)]
    return t[rint(len(t)) - 1]


def transpose(t):
    """
    _summary_

    Args:
        t (_type_): _description_

    Returns:
        _type_: _description_
    """

    u = []

    for i in range(len(t[0])):
        u.append([])

        for j in range(len(t)):
            u[i].append(t[j][i])

    return u


def dofile(sFile):
    """
    Turns sFile into JSON and returns a dictionary version of the file contents.

    Args:
        sFile (str): Filename to be turned into JSON.

    Returns:
        dict: Dictionary version of the file contents.
    """

    with open(sFile) as src:
        contents = src.read()

        returned = contents[contents.index("return {") + len("return {"):contents.rindex("}")].replace("domain", "\"domain\"").replace(
            "cols", "\"cols\"").replace("rows", "\"rows\"").replace("=", ":").replace("'", "\"").replace("{", "[").replace("}", "]").replace("_", "\"\"")

        dictionary = json.loads("{{{}}}".format(returned))

    return dictionary


def repCols(cols):
    """
    _summary_

    Args:
        cols (dict): _description_

    Returns:
        DATA: _description_
    """

    cols = copy.deepcopy(cols)

    for col in cols:
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]

        for i in range(len(col) - 1):
            col[i] = col[i + 1]

        col.pop()

    def fun(k):
        return "Num" + str(k)

    cols.insert(0, list(map(fun, range(1, len(cols[0]) + 1))))
    cols[0][len(cols[0]) - 1] = "thingX"

    return data.DATA(cols)


def repRows(t, rows):
    """
    _summary_

    Args:
        t (_type_): _description_
        rows (_type_): _description_

    Returns:
        _type_: _description_
    """

    rows = copy.deepcopy(rows)

    for j, s in enumerate(rows[-1]):
        rows[0][j] = rows[0][j] + ":" + s

    rows.pop()

    for n, row in enumerate(rows):
        if n == 0:
            row.append("thingX")
        else:
            u = t["rows"][-n]
            row.append(u[-1])

    return data.DATA(rows)


def repPlace(data, n=20, g=[]):
    """
    _summary_

    Args:
        data (_type_): _description_
        n (int, optional): _description_. Defaults to 20.
        g (dict, optional): _description_. Defaults to [].
        maxy (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """

    for i in range(n):
        g.append([])

        for _ in range(n):
            g[i].append(" ")

    print("")

    maxy = 0
    for r, row in enumerate(data.rows):
        c = chr(64 + r)

        print(c, row.cells[-1])

        x = int(row.x * n)
        y = int(row.y * n)
        maxy = max(maxy, y + 1)
        g[y + 1][x + 1] = c

    print("")

    for i in range(maxy):
        print("[{}]".format(" ".join(g[i])))


def repgrid(sFile):
    """
    _summary_

    Args:
        sFile (_type_): _description_

    Returns:
        _type_: _description_
    """

    t = dofile(sFile)
    rows = repRows(t, transpose(t["cols"]))
    cols = repCols(t["cols"])

    show(rows.cluster())
    show(cols.cluster())
    repPlace(rows)


def show(node, what="mid", lvl=0):
    """
    Prints the tree version of DATA.

    Args:
        node (dict): Dictionary of DATA to be printed.
        what (str): Either "mid" or "div". Defaults to "mid".
        lvl (int, optional): Current tree level. Defaults to 0.
    """

    if node:
        print("|.. " * lvl, end="")

        print(node["data"].rows[-1].cells[-1]
              if "left" not in node else round(100 * node["c"]))

        if "left" in node:
            show(node["left"], what, lvl + 1)

        if "right" in node:
            show(node["right"], what, lvl + 1)

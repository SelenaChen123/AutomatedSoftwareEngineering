import math
import re


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


def copy(t):
    """
    Deep copies t.

    Args:
        t (_type_): _description_

    Returns:
        _type_: _description_
    """

    print("Not yet implemented")
    return 0


def transpose(t):
    """
    _summary_

    Args:
        t (_type_): _description_

    Returns:
        _type_: _description_
    """

    print("Not yet implemented")
    return 0


def repCols(cols):
    """
    _summary_

    Args:
        cols (_type_): _description_

    Returns:
        _type_: _description_
    """

    print("Not yet implemented")
    return 0


def repRows(t, rows, u):
    """
    _summary_

    Args:
        t (_type_): _description_
        rows (_type_): _description_
        u (_type_): _description_

    Returns:
        _type_: _description_
    """

    print("Not yet implemented")
    return 0


def repPlace(data, n=20, g={}, maxy=0):
    """
    _summary_

    Args:
        data (_type_): _description_
        n (int, optional): _description_. Defaults to 20.
        g (dict, optional): _description_. Defaults to {}.
        maxy (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """

    print("Not yet implemented")
    return 0


def repgrid(file):
    """
    _summary_

    Args:
        file (_type_): _description_

    Returns:
        _type_: _description_
    """

    print("Not yet implemented")
    return 0


def show(node, what, cols, nPlaces, lvl=0):
    """
    Prints the tree version of DATA.

    Args:
        node (dict): Dictionary of DATA to be printed.
        what (str): Either "mid" or "div".
        cols (list): Columns that the stats are being taken from.
        nPlaces (int): Number of places to round the stats to.
        lvl (int, optional): Current tree level. Defaults to 0.
    """

    print("Not yet implemented")
    return 0

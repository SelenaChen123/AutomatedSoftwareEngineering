import creation
import globals
import utils


def row(data, t):
    """
    Adds a new row to data and updates column headers.

    Args:
        data (dict): Dictionary of data to add a new row to.
        t (list): Row to be added.

    Returns:
        dict: Updated dictionary of data.
    """

    if data["cols"]:
        data["rows"].append(t)

        for cols in [data["cols"]["x"], data["cols"]["y"]]:
            for col in cols:
                add(col, t[col["at"]])
    else:
        data["cols"] = creation.COLS(t)

    return data


def add(col, x, n=1):
    """
    Adds x to col.

    Args:
        col (dict): Column to add x to.
        x (int): Value to be added to col.
        n (int, optional): Threshold for any random item to be replaced by x if the max is reached. Defaults to 1.
    """

    def sym(t):
        if x in t:
            t[x] = n + t[x]
        else:
            t[x] = n

        if t[x] > col["most"]:
            col["most"] = t[x]
            col["mode"] = x

    def num(t):
        col["lo"] = min(x, col["lo"])
        col["hi"] = max(x, col["hi"])

        if len(t) < globals.Is["Max"]:
            col["ok"] = False
            t.append(x)
        elif utils.rand() < globals.Is["Max"] / col["n"]:
            col["ok"] = False
            t[utils.rint(1, len(t)) - 1] = x

    if x != "?":
        col["n"] += n

        if "isSym" in col:
            sym(col["has"])
        else:
            num(col["has"])


def adds(col, t=[]):
    """
    Adds the items from t to col.

    Args:
        col (dict): Column to add x to.
        t (list, optional): List of items to be added to col. Defaults to [].

    Returns:
        dict: Updated col.
    """

    for x in t:
        add(col, x)

    return col


def extend(Range, n, s):
    """
    Updates a range to cover n and s.

    Args:
        Range (dict): Range to be updated.
        n (int): x value to update Range to cover.
        s (str): y value to update Range to cover.
    """

    Range["lo"] = min(n, Range["lo"])
    Range["hi"] = max(n, Range["hi"])

    add(Range["y"], s)

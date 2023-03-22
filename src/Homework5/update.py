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

    if x != "?":
        col["n"] += n

        if "isSym" in col:
            if x in col["has"]:
                col["has"][x] = n + col["has"][x]
            else:
                col["has"][x] = n

            if col["has"][x] > col["most"]:
                col["most"] = col["has"][x]
                col["mode"] = x
        else:
            col["lo"] = min(x, col["lo"])
            col["hi"] = max(x, col["hi"])

            if len(col["has"]) < globals.the["Max"]:
                pos = len(col["has"]) + 1
            else:
                if utils.rand() < globals.the["Max"] / col["n"]:
                    pos = utils.rint(1, len(col["has"]))
                else:
                    pos = -1

            if pos > -1:
                if len(col["has"]) >= pos:
                    col["has"][pos - 1] = x
                else:
                    col["has"].append(x)

                col["ok"] = False


def adds(col, t=[]):
    """
    Adds the items from t to col.

    Args:
        col (dict): Column to add the items to.
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

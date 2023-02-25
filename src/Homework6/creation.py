import math
import re


def COL(n, s):
    """
    Creates a COL that represents either a NUM or a SYM.

    Args:
        n (int): Column position.
        s (str): Name.

    Returns:
        dict: Created COL.
    """

    col = NUM(n, s) if re.search("^[A-Z]+", s) else SYM(n, s)

    col["isIgnored"] = re.search("X$", s) != None
    col["isKlass"] = re.search("!$", s) != None
    col["isGoal"] = re.search("[!+-]$", s) != None

    return col


def NUM(n=0, s=""):
    """
    Creates a NUM to summarize a stream of numbers.

    Args:
        n (int, optional): Column position. Defaults to 0.
        s (str, optional): Name. Defaults to "".

    Returns:
        dict: Created NUM.
    """

    return {"at": n, "txt": s, "n": 0, "hi": -math.inf, "lo": math.inf, "ok": True, "has": [], "w": -1 if "-" in s else 1}


def SYM(n=0, s=""):
    """
    Creates a SYM to summarize a stream of symbols.

    Args:
        n (int, optional): Column position. Defaults to 0.
        s (str, optional): Name. Defaults to "".

    Returns:
        dict: Created SYM.
    """

    return {"at": n, "txt": s, "n": 0, "mode": None, "most": 0, "isSym": True, "has": {}}


def COLS(ss):
    """
    Creates a set of COLs.

    Args:
        ss (list): Names of the columns.

    Returns:
        dict: Created COLS.
    """

    cols = {"names": ss, "all": [], "x": [], "y": []}

    for n, s in enumerate(ss):
        col = COL(n, s)
        cols["all"].append(col)

        if not col["isIgnored"]:
            if col["isKlass"]:
                cols["klass"] = col

            if col["isGoal"]:
                cols["y"].append(col)
            else:
                cols["x"].append(col)

    return cols


def RANGE(at, txt, lo=0, hi=1):
    """
    Creates a RANGE that tracks the dependent values seen in the range between lo to hi for some independent variable in column position at whose name is txt.

    Args:
        at (int): Column position.
        txt (_type_): Column name.
        lo (int, optional): Lower bound for the range. Defaults to 0.
        hi (int, optional): Upper bound for the range. Defaults to 1.

    Returns:
        dict: Created RANGE.
    """

    return {"at": at, "txt": txt, "lo": lo, "hi": lo or hi, "y": SYM()}


def RULE(ranges, maxSize):
    return "NOT YET IMPLEMENTED"


def prune(rule, maxSize):
    return "NOT YET IMPLEMENTED"


def DATA(src, rows, data, add):
    return "NOT YET IMPLEMENTED"

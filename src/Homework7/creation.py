import update


def NUM(t=[]):
    """
    Creates a NUM to summarize a stream of numbers.

    Args:
        t (list, optional): List of items to create a NUM from. Defaults to [].

    Returns:
        dict: Created NUM.
    """
    i = {"n": 0, "mu": 0, "m2": 0, "sd": 0}

    for x in t:
        update.add(i, x)

    return i


def RX(t, s=""):
    """
    Creates an RX.

    Args:
        t (list): List of items to create an RX from.
        s (str, optional): Name of the RX. Defaults to "".

    Returns:
        dict: Created RX.
    """

    return {"name": s, "rank": 0, "n": len(t), "show": "", "has": sorted(t)}

def add(i, x):
    """
    Adds x to i.

    Args:
        i (dict): Dictionary to add x to.
        x (int): Value to be added to i.

    Returns:
        dict: Updated i.
    """

    i["n"] += 1
    d = x - i["mu"]
    i["mu"] += d / i["n"]
    i["m2"] += d * (x - i["mu"])
    i["sd"] = 0 if i["n"] < 2 else (i["m2"] / (i["n"] - 1)) ** .5

    return i

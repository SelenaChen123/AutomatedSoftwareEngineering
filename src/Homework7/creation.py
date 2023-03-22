import utils


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
        utils.add(i, x)

    return i


def RX(t, s):
    print("NOT YET IMPLEMENTED")

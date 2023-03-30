def mid(t):
    """
    Returns the central tendency of t.

    Args:
        t (dict): Dictionary to get the central tendency of.

    Returns:
        float: Central tendency of t.
    """

    t = t["has"] if t["has"] else t

    return (t[(len(t) - 1) // 2] + t[(len(t) - 1) // 2 + 1]) / 2 if len(t) % 2 == 0 else t[(len(t) - 1) // 2 + 1]


def div(t):
    """
    Returns the deviation of t from its central tendency.

    Args:
        t (dict): Dictionary to get the deviation from its central tendency.

    Returns:
        int/float: Deviation from its central tendency of t.
    """

    t = t["has"] if "has" in t else t

    return (t[len(t) * 9 // 10] - t[len(t) * 1 // 10]) / 2.56

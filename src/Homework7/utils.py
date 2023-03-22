import math

import globals


def samples(t, n):
    """
    Returns n samples from t.

    Args:
        t (list): List to return the samples from.
        n (int): Number of samples to be returned.

    Returns:
        list: List of n samples from t.
    """

    return [t[math.randint(len(t)) - 1] for _ in range(0, n)]


def cliffsDelta(ns1, ns2):
    """
    Returns whether or not the Cliff's Delta between ns1 and ns2 is greater than the global cliffs threshold.

    Args:
        ns1 (list): First list to calculate the Cliff's Delta from.
        ns2 (list): Second list to calculate the Cliff's Delta from.

    Returns:
        bool: True if the Cliff's Delta between ns1 and ns2 is greater than the global cliffs threshold, False otherwise.
    """

    if len(ns1) > 128:
        ns1 = samples(ns1, 128)

    if len(ns2) > 128:
        ns2 = samples(ns2, 128)

    n = 0
    gt = 0
    lt = 0

    for x in ns1:
        for y in ns2:
            n += 1

            if x > y:
                gt += 1

            if x < y:
                lt += 1

    return abs(lt - gt) / n <= globals.the["cliffs"]


def gaussian(mu=0, sd=1):
    """
    Returns a sample from a Gaussian with mean mu and standard deviation sd.

    Args:
        mu (int, optional): Mean of the Gaussian. Defaults to 0.
        sd (int, optional): Standard deviation of the Gaussian. Defaults to 1.

    Returns:
        float: Sample from a Gaussian with mean mu and standard deviation sd.
    """

    return mu + sd * math.sqrt(-2 * math.log(math.random())) * math.cos(2 * math.pi * math.random())


def delta(i, other):
    """
    Returns the delta between i and other.

    Args:
        i (dict): first dictionary to calculate the delta from.
        other (dict): Second dictionary to calculate the delta from.

    Returns:
        float: Delta between i and other.
    """

    return abs(i["mu"] - other["mu"]) / ((1E-32 + i["sd"] ** 2 / i["n"] + other["sd"] ** 2 / other["n"]) ** .5)

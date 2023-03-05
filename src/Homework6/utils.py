import math
import re

import globals


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


def rand(nlo=0, nhi=1):
    """
    Generates a random float between nlo (inclusive) and nhi (not inclusive).

    Args:
        nlo (int, optional): Lower bound for the random float generation. Defaults to 0.
        nhi (int, optional): Upper bound for the random float generation. Defaults to 1.

    Returns:
        float: Random float between nlo (inclusive) and nhi (not inclusive).
    """

    globals.seed = (16807 * globals.seed) % 2147483647

    return nlo + (nhi - nlo) * globals.seed / 2147483647


def rint(nlo=0, nhi=1):
    """
    Generates a random int between nlo (inclusive) and nhi (not inclusive).

    Args:
        nlo (int, optional): Lower bound for the random int generation. Defaults to 0.
        nhi (int, optional): Upper bound for the random int generation. Defaults to 1.

    Returns:
        int: Random int between nlo (inclusive) and nhi (not inclusive).
    """

    return math.floor(0.5 + rand(nlo, nhi))


def per(t, p=.5):
    """
    Returns the p-ratio item in t.

    Args:
        t (list): List to return the p-ratio item from.
        p (float, optional): Ratio of the item to be returned from t. Defaults to .5.

    Returns:
        int/float: p-ratio item in t.
    """

    p = math.floor(p * len(t) + .5)

    return t[max(min(p, len(t)) - 1, 0)]


def many(t, n):
    """
    Returns n items from t.

    Args:
        t (list): List to return the items from.
        n (int): Number of items to be returned.

    Returns:
        list: List of n items from t.
    """

    return [any(t) for _ in range(0, n)]


def any(t):
    """
    Returns a random item from t.

    Args:
        t (list): List to return the random item from.

    Returns:
        ROW: Random item from t.
    """

    # return t[rint(0, len(t) - 1)]
    return t[rint(len(t)) - 1]


def cliffsDelta(ns1, ns2):
    """
    Returns whether or not the Cliff's Delta between ns1 and ns2 is greater than the global cliffs threshold.

    Args:
        ns1 (list): First list to calculate the Cliff's Delta from.
        ns2 (list): Second list to calculate the Cliff's Delta from.

    Returns:
        bool: True if the Cliff's Delta between ns1 and ns2 is greater than the global cliffs threshold, False otherwise.
    """

    if len(ns1) > 256:
        ns1 = many(ns1, 256)

    if len(ns2) > 256:
        ns2 = many(ns2, 256)

    if len(ns1) > 10 * len(ns2):
        ns1 = many(ns1, 10 * len(ns2))

    if len(ns2) > 10 * len(ns1):
        ns2 = many(ns2, 10 * len(ns1))

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

    return abs(lt - gt) / n > globals.Is["cliffs"]


def diffs(nums1, nums2):
    """
    Reports whether or not num1 and num2 have different values.

    Args:
        nums1 (dict): First dictionary of data to check the difference of.
        nums2 (dict): Second dictionary of data to check the difference of.

    Returns:
        dict: Report of whether or not num1 and num2 have different values.
    """

    def function(nums):
        return nums["txt"], cliffsDelta(nums["has"], nums2[0]["has"])

    return dict(sorted(map(function, nums1)))

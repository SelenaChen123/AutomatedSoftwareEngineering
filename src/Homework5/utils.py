import math
import re


seed = 937162211


def coerce(s):
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
    with open(sFilename) as src:
        lines = src.readlines()

        for s in lines:
            t = []

            for s1 in re.findall("([^,]+)", s):
                t.append(coerce(s1))

            fun(t)


def rand(nlo=0, nhi=1):
    global seed
    seed = (16807 * seed) % 2147483647
    return nlo + (nhi - nlo) * seed / 2147483647


def rint(nlo, nhi=1):
    return math.floor(0.5 + rand(nlo, nhi))


def per(t, p):
    p = math.floor((p or .5) * len(t) + .5)

    return t[max(min(p, len(t)), 1)]


def many(t, n):
    return [any(t) for _ in range(0, n)]


def any(t):
    # return t[rint(0, len(t) - 1)]
    return t[rint(len(t)) - 1]


def cliffsDelta(ns1, ns2):
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

    return math.abs(lt - gt) / n > globals.the["cliffs"]


def diffs(nums1, nums2):
    def function(k, nums):
        return cliffsDelta(nums.has, nums2[k].has), nums.txt

    return map(function, nums1)

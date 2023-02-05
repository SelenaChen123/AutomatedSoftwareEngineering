import random
import re
import math
import globals


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


def lt(a, b):
    return a["dist"] < b["dist"]


def cosine(a, b, c):
    x1 = (a ** 2 + c ** 2 - b ** 2)

    if c != 0:
        x1 = x1 / (2 * c)

    x2 = max(0, min(1, x1))
    y = (a ** 2 - x2 ** 2) ** 0.5

    return x2, y

Seed=937162211

def rand(lo,hi):
  global Seed
  lo  = lo or 0
  hi = hi or 1  
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces = 3):  
    mult = 10**(nPlaces)
    return math.floor((n * mult + 0.5) / mult)

def many(t, n):
    return [any(t) for _ in range(0, n)]

def rint(lo,hi = None):
    return math.floor(0.5 + rand(lo,hi))

def any(t):
    return t[rint(len(t))-1]

def show(node, what, cols, nPlaces, lvl=0):
    if "data" in node:
        print("{} {}  ".format("| " * lvl, len(node["data"].rows)), end="")

        print(node["data"].stats("mid", node["data"].cols.y, nPlaces)
              if "left" not in node or lvl == 0 else "")

        if "left" in node:
            show(node["left"], what, cols, nPlaces, lvl + 1)

        if "right" in node:
            show(node["right"], what, cols, nPlaces, lvl + 1)

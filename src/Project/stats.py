import math

import creation
import globals
import query
import update
import utils


def bootstrap(y0, z0):
    """
    Returns whether or not y0 and z0 are similar using the bootstrap procedure.

    Args:
        y0 (list): First list of samples to use the bootstrap procedure on.
        z0 (list): Second list of samples to use the bootstrap procedure on.

    Returns:
        bool: True if y0 and z0 are similar, False otherwise.
    """

    x = creation.NUM()
    y = creation.NUM()
    z = creation.NUM()
    yhat = []
    zhat = []

    for y1 in y0:
        update.update_num_keys(x, y1)
        update.update_num_keys(y, y1)

    for z1 in z0:
        update.update_num_keys(x, z1)
        update.update_num_keys(z, z1)

    for y1 in y0:
        yhat.append(y1 - y["mu"] + x["mu"])

    for z1 in z0:
        zhat.append(z1 - z["mu"] + x["mu"])

    n = 0

    for _ in range(globals.Is["bootstrap"]):
        if utils.delta(creation.NUM(t=utils.samples(yhat)), creation.NUM(t=utils.samples(zhat))) > utils.delta(y, z):
            n += 1

    return n / globals.Is["bootstrap"] >= globals.Is["conf"]


def merge(rx1, rx2):
    """
    Merges rx1 and rx2.

    Args:
        rx1 (RX): First RX to be merged.
        rx2 (RX): Second RX to be merged.

    Returns:
        dict: Merged version of rx1 and rx2.
    """

    rx3 = creation.RX([], rx1["name"])

    for t in [rx1["has"], rx2["has"]]:
        for x in t:
            rx3["has"].append(x)

    rx3["has"] = sorted(rx3["has"])
    rx3["n"] = len(rx3["has"])

    return rx3


def scottKnot(rxs):
    """
    Ranks RXs using the Scott-Knot procedure.

    Args:
        rxs (list): List of RXs to be ranked.

    Returns:
        list: List of RXs with ranks.
    """

    def merges(i, j):
        out = creation.RX([], rxs[i]["name"])

        for _ in range(i, j + 1):
            out = merge(out, rxs[j])

        return out

    def same(lo, cut, hi):
        l = merges(lo, cut)
        r = merges(cut + 1, hi)

        return bootstrap(l["has"], r["has"]) if utils.cliffsDelta(l["has"], r["has"]) else None

    def recurse(lo, hi, rank):
        b4 = merges(lo, hi)
        cut = None
        best = 0

        for i in range(lo, hi + 1):
            if i < hi:
                l = merges(lo, i)
                r = merges(i + 1, hi)
                now = (l["n"] * (query.mid1(l) - query.mid1(b4)) ** 2 + r["n"]
                       * (query.mid1(r) - query.mid1(b4)) ** 2) / (l["n"] + r["n"])

                if now > best:
                    if abs(query.mid1(l) - query.mid1(r)) >= cohen:
                        cut = i
                        best = now

        if cut != None and not same(lo, cut, hi):
            rank = recurse(lo, cut, rank) + 1
            rank = recurse(cut + 1, hi, rank)
        else:
            for i in range(lo, hi + 1):
                rxs[i]["rank"] = rank

        return rank

    rxs = sorted(rxs, key=lambda x: query.mid1(x))
    cohen = query.div1(
        merges(0, len(rxs) - 1)) * globals.Is["cohen"]
    recurse(0, len(rxs) - 1, 1)

    return rxs


def tiles(rxs):
    """
    Generates the box plots of the RXs.

    Args:
        rxs (list): List of RXs to generate box plots for.

    Returns:
        list: List of RXs with box plots.
    """

    lo = math.inf
    hi = -math.inf

    for rx in rxs:
        lo = min(lo, rx["has"][0])
        hi = max(hi, rx["has"][len(rx["has"]) - 1])

    for rx in rxs:
        t, u = rx['has'], []

        def of(x, most):
            return int(max(1, min(most, x)))

        def at(x):
            return t[of(len(t)*x//1, len(t))]

        def pos(x):
            return math.floor(of(40*(x-lo)/(hi-lo+1E-32)//1, 40))

        for _ in range(globals.Is["width"] + 1):
            u.append(" ")

        for i in range(pos(at(.1)), pos(at(.3)) + 1):
            u[i] = "-"

        for i in range(pos(at(.7)), pos(at(.9)) + 1):
            u[i] = "-"

        u[globals.Is["width"] // 2] = "|"
        u[pos(at(.5))] = "*"

        rx["show"] = "".join(u) + " {" + "{:6.2f}".format(at(.1))

        for x in [at(.3), at(.5), at(.7), at(.9)]:
            rx["show"] += ", " + "{:6.2f}".format(x)

        rx["show"] += " }"

    return rxs

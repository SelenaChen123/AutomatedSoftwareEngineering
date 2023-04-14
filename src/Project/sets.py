import creation
import discretization
import query
import utils


def xpln(data, best, rest):
    """
    Collects all of the ranges into a flat list and sorts them by their values.

    Args:
        data (dict): Dictionary of data to be sorted.
        best (dict): Best half of the data.
        rest (dict): Rest of the data.
    """

    def score(ranges):
        rule = creation.RULE(ranges, maxSizes)

        if rule:
            print(showRule(rule))

            bestr = selects(rule, best["rows"])
            restr = selects(rule, rest["rows"])

            if len(bestr) + len(restr) > 0:
                return query.value({"best": len(bestr), "rest": len(restr)}, len(best["rows"]), len(rest["rows"]), "best"), rule

        return None, None

    tmp = []
    maxSizes = {}

    for ranges in discretization.bins(data["cols"]["x"], {"best": best["rows"], "rest": rest["rows"]}):
        maxSizes[ranges[0]["txt"]] = len(ranges)

        print("")

        for Range in ranges:
            print(Range["txt"], Range["lo"], Range["hi"])

            tmp.append({"range": Range, "max": len(ranges),
                       "val": query.value(Range["y"]["has"], len(best["rows"]), len(rest["rows"]), "best")})

    return firstN(sorted(tmp, key=lambda x: x["val"], reverse=True), score)


def firstN(sortedRanges, scoreFun):
    """
    Returns the best ranges according to their values.

    Args:
        sortedRanges (list): Sorted list of ranges to return the best ranges from.
        scoreFun (function): Score function to determine the values of the ranges.

    Returns:
        dict: Best ranges according to the values.
        most: Best value.
    """

    print("")

    def function(r):
        print(r["range"]["txt"], r["range"]["lo"], r["range"]
              ["hi"], round(r["val"], 2), r["range"]["y"]["has"])

    list(map(function, sortedRanges))
    first = sortedRanges[0]["val"]

    def useful(Range):
        return Range if Range["val"] > .05 and Range["val"] > first / 10 else None

    sortedRanges = list(map(useful, sortedRanges))

    most = -1
    out = None

    for i in range(len(sortedRanges)):
        if sortedRanges[i]:
            tmp, rule = scoreFun(
                list(map(lambda x: x["range"], sortedRanges[:i + 1])))

            if tmp and tmp > most:
                out = rule
                most = tmp

    return out, most


def showRule(rule):
    """
    Prints rule.

    Args:
        rule (dict): Rule to be printed.

    Returns:
        dict: Rule that was printed.
    """

    def pretty(Range):
        return Range["lo"] if Range["lo"] == Range["hi"] else [Range["lo"], Range["hi"]]

    def merges(attr, ranges):
        return list(map(pretty, merge(sorted(ranges, key=lambda x: x["lo"])))), attr

    def merge(t0):
        t = []
        i = 1

        while i <= len(t0):
            left = t0[i - 1]
            right = t0[i] if i < len(t0) else None

            if right and left["hi"] == right["lo"]:
                left["hi"] == right["hi"]
                i += 1

            t.append({"lo": left["lo"], "hi": left["hi"]})
            i += 1

        return t if len(t0) == len(t) else merge(t)

    return utils.kap(rule, merges)


def selects(rule, rows):
    """
    Returns the conjunctions from the ranges in rule.

    Args:
        rule (dict): Rule to return the conjunctions from.
        rows (list): List of rows used to find the conjunctions from.

    Returns:
        list: List of conjunctions from the ranges in rule.
    """

    def disjunction(ranges, row):
        for Range in ranges:
            if row[Range["at"]] == "?" or (Range["lo"] == Range["hi"] and Range["lo"] == row[Range["at"]]) or (Range["lo"] <= row[Range["at"]] and row[Range["at"]] < Range["hi"]):
                return True

        return False

    def conjunction(row):
        for ranges in rule.values():
            if not disjunction(ranges, row):
                return False

        return True

    def function(r):
        return r if conjunction(r) else None

    return [item for item in list(map(function, rows)) if item]

import creation
import discretization
import query


def xpln(data, best, rest):
    def score(ranges, rule, bestr, restr):
        global maxSizes
        rule = creation.RULE(ranges, maxSizes)

        if rule:
            print(showRule(rule))

            bestr = selects(rule, best["rows"])
            restr = selects(rule, rest["rows"])

            if len(bestr) + len(restr) > 0:
                return query.value({"best": len(bestr), "rest": len(restr)}, len(best["rows"]), len(rest["rows"]), "best")

    tmp = []
    maxSizes = {}

    for ranges in discretization.bins(data["cols"]["x"], {"best": best["rows"], "rest": rest["rows"]}):
        maxSizes[ranges[0]["txt"]] = len(ranges)

        print("")

        for Range in ranges:
            print(Range["txt"], Range["lo"], Range["hi"])

            tmp.append({"range": Range, "max": len(ranges),
                       "val": query.value(Range["y"]["has"])})

    return firstN(sorted(tmp, key=lambda x: x["val"], reverse=True), score)


def firstN(sortedRanges, scoreFun):
    print("")

    def function(r):
        print(r["range"]["txt"], r["range"]["lo"], r["range"]
              ["hi"], round(r["val"], 2), r["range"]["y"]["has"])

    map(function, sortedRanges)

    def useful(Range):
        global first
        return Range if Range["val"] > .05 and Range["val"] > first / 10 else None

    sortedRanges = map(useful, sortedRanges)

    most = -1
    out = None

    for i in range(len(sortedRanges)):
        tmp, rule = scoreFun(map(lambda x: x["range"], sortedRanges[:i]))

        if tmp and tmp > most:
            out = rule
            most = tmp

    return out, most


def showRule(rule):
    def pretty(Range):
        return Range["lo"] if Range["lo"] == Range["hi"] else [Range["lo"], Range["hi"]]

    def merges(attr, ranges):
        return map(pretty, merge(sorted(ranges, key=lambda x: x["lo"]))), attr

    def merge(t0):
        t = []
        i = 1

        while i <= len(t0):
            left = t0[i - 1]
            right = t0[i]

            if right and left["hi"] == right["lo"]:
                left["hi"] == right["hi"]
                i += 1

                t.append({"lo": left["lo"], "hi": left["hi"]})
                i += 1

        return t if len(t0) == len(t) else merge(t)

    return [merges(r[0], r[1]) for r in rule]


def selects(rule, rows):
    def disjunction(ranges, row):
        for Range in ranges:
            if row[Range["at"]] == "?" or Range["lo"] == Range["hi"] and Range["lo"] == Range["at"] or Range["lo"] <= Range["at"] and Range["at"] < Range["hi"]:
                return True

        return False

    def conjunction(row):
        for ranges in rule:
            if not disjunction(ranges, row):
                return False

        return True

    def function(r):
        return r if conjunction(r) else None

    return map(function, rows)

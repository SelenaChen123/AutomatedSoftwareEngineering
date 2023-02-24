import clustering
import creation
import globals
import utils
import query


def sway(data):
    def worker(rows, worse):
        if len(rows) <= len(data["rows"]) ** globals.the["min"]:
            return rows, utils.many(worse, globals.the["rest"] * len(rows))
        else:
            l, r, A, B, _ = clustering.half(data, rows)

            if query.better(data, B, A):
                l, r, A, B = r, l, B, A

            def function(row):
                return worse.append(row)

            map(function, r)

            return worker(l, worse)

    best, rest = worker(data["rows"], [])

    return creation.clone(data, best), creation.clone(data, rest)

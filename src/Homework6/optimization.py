import clustering
import creation
import globals
import query
import utils


def sway(data):
    """
    Recursively returns the best half of the dictionary of data.

    Args:
        data (dict): Dictionary of data to return the best half of.

    Returns:
        dict: Dictionary of remaining DATA to recursively return the best half of.
    """

    def worker(rows, worse, above=[]):
        if len(rows) <= len(data["rows"]) ** globals.the["min"]:
            return rows, utils.many(worse, globals.the["rest"] * len(rows))
        else:
            l, r, A, B, _ = clustering.half(data, rows, None, above)

            if query.better(data, B, A):
                l, r, A, B = r, l, B, A

            def function(row):
                return worse.append(row)

            list(map(function, r))

            return worker(l, worse, A)

    best, rest = worker(data["rows"], [])

    return creation.clone(data, best), creation.clone(data, rest)

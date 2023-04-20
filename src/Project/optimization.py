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

    def worker(rows, worse, evals0, above=[]):
        if len(rows) <= len(data["rows"]) ** globals.Is["min"]:
            return rows, utils.many(worse, globals.Is["rest"] * len(rows)), evals0
        else:
            l, r, A, B, _, evals = clustering.half(data, rows, None, above)

            if query.better(data, B, A):
                l, r, A, B = r, l, B, A

            def function(row):
                return worse.append(row)

            list(map(function, r))

            return worker(l, worse, evals + evals0, A)

    best, rest, evals = worker(data["rows"], [], 0)

    return creation.DATA(data, best), creation.DATA(data, rest), evals


def sway2(data):
    """
    Recursively returns the best half of the dictionary of data.

    Args:
        data (dict): Dictionary of data to return the best half of.

    Returns:
        dict: Dictionary of remaining DATA to recursively return the best half of.
    """

    def worker(rows, worse, evals0, above=[]):
        if len(rows) <= len(data["rows"]) ** globals.Is["min"]:
            return rows, utils.many(worse, globals.Is["rest"] * len(rows)), evals0
        else:
            l, r, A, B, _, evals = clustering.half2(data, rows, None, above)

            if query.better(data, B, A):
                l, r, A, B = r, l, B, A

            def function(row):
                return worse.append(row)

            list(map(function, r))

            return worker(l, worse, evals + evals0, A)

    best, rest, evals = worker(data["rows"], [], 0)

    return creation.DATA(data, best), creation.DATA(data, rest), evals

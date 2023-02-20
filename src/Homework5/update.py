
import creation
import globals
import utils


def row(data, t):
    if data["cols"]:
        data["rows"].append(t)

        for cols in [data["cols"]["x"], data["cols"]["y"]]:
            for col in cols:
                add(col, t[col["at"]])
    else:
        data["cols"] = creation.COLS(t)

    return data


def add(col, x, n=1):
    if x != "?":
        col["n"] += n

        if col.get("isSym"):
            x = int(x)
            if len(col['has']) >= x + 1:
                col["has"][x] = n + col["has"][x]
            else:
                col['has'].append(n)

            if col["has"][x] > col["most"]:
                col["most"] = col["has"][x]
                col["mode"] = x
        else:
            col["lo"] = min(x, col["lo"])
            col["hi"] = max(x, col["hi"])

            if len(col["has"]) < globals.the["Max"]:
                pos = len(col["has"])
            else:
                if utils.rand() < globals.the["Max"] / col["n"]:
                    pos = utils.rint(0, len(col["has"]))
                else:
                    pos = -1

            if pos >= 0:
                col["has"].append(x)
                col["ok"] = False


def adds(col, t):
    for x in t or []:
        add(col, x)

    return col


def extend(Range, n, s):
    Range["lo"] = min(n, Range["lo"])
    Range["hi"] = max(n, Range["hi"])

    add(Range["y"], s)

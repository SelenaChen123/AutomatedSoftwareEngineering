import math
import re

import update
import utils


def COL(n, s):
    col = NUM(n, s) if re.search("^[A-Z]+", s) else SYM(n, s)

    col["isIgnored"] = re.search("X$", s)
    col["isKlass"] = re.search("!$", s)
    col["isGoal"] = re.search("[!+-]$", s)

    return col


def NUM(n=0, s=""):
    return {"at": n, "txt": s, "n": 0, "hi": -math.inf, "lo": math.inf, "ok": True, "has": [], "w": -1 if "-" in s else 1}


def SYM(n=0, s=""):
    return {"at": n or 0, "txt": s or "", "n": 0, "mode": None, "most": 0, "isSym": True, "has": []}


def COLS(ss):
    cols = {"names": ss, "all": [], "x": [], "y": []}

    for n, s in enumerate(ss):
        col = COL(n, s)
        cols["all"].append(col)

        if not col["isIgnored"]:
            if col["isKlass"]:
                cols["klass"] = col

                cols["y" if col["isGoal"] else "x"].append(col)

    return cols


def RANGE(at, txt, lo, hi):
    return {"at": at, "txt": txt, "lo": lo, "hi": lo or hi, "y": SYM()}


def new():
    return {"rows": [], "cols": None}


def read(sfile):
    data = new()

    def function(t):
        update.row(data, t)

    utils.csv(sfile, function)

    return data


def clone(data, ts):
    data1 = update.row(new(), data["cols"]["names"])

    for t in ts or []:
        update.row(data1, t)

    return data1

import re


def map(t, fun):
    u = {}

    for k, v in enumerate(t):
        v, k = fun(v)

        if k and k != False:
            u[k] = v
        else:
            u[1 + len(u)] = v

    return u


def kap(t, fun):
    u = {}

    for k, v in t.items():
        v, k = fun(k, v)

        if k and k != False:
            u[k] = v
        else:
            u[1 + len(u)] = v

    return u


def keys(self, t):
    return sorted(self.kap(t.keys()))


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

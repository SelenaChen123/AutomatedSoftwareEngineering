def map(t, fun):
    u = {}

    for k, v in t.items():
        v, k = fun(v)
        if k != None and k != False:
            u[k] = v
        else:
            u[1 + len(u)] = v

    return u


def kap(t, fun):
    u = {}

    for k, v in t.items():
        v, k = fun(k, v)
        if k != None and k != False:
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

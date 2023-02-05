def map(t, fun):
    """
    Map a function "fun(v)" over list (skip all nil results)

    Args:
        t (dict): dictionary containing the list of items to be mapped
        fun (func): a function that will map the items in t

    Returns:
        dict: dictionary that functions as a map of items to their values 
            from the function "fun(v)" 
    """
    u = {}

    for k, v in t.items():
        v, k = fun(v)
        if k != None and k != False:
            u[k] = v
        else:
            u[1 + len(u)] = v

    return u


def kap(t, fun):
    """
    Map a function "fun(k,v)" over list (skip all nil results)

    Args:
        t (dict): dictionary containing the list of items to be mapped
        fun (func): a function that will map the items in t

    Returns:
        dict: dictionary that functions as a map of items to their values 
            from the function "fun(k,v)" 
    """
    u = {}

    for k, v in t.items():
        v, k = fun(k, v)
        if k != None and k != False:
            u[k] = v
        else:
            u[1 + len(u)] = v

    return u


def keys(self, t):
    """
    Return the list of table keys, sorted

    Args:
        t (dict): list of values

    Returns:
        dict: a version of the dictionary sorted by key
    """
    return sorted(self.kap(t.keys()))


def coerce(s):
    """
    Return int or float or bool or string from "s"

    Args:
        s (string): string that results in one of four different variable outputs

    Returns:
        int,float,bool,str: returns a value according to what the string has
    """
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

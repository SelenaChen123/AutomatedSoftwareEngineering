def coerce(s):
    """
    Coerces a str s into an int, float, bool, or trimmed str.

    Args:
        s (str): Str to be coerced into an int, float, bool, or trimmed str.

    Returns:
        int/float/bool/str: int, float, bool, or trimmed str version of s.
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

import math


class SYM:
    """
    Summarizes a stream of symbols.
    """

    def __init__(self, at=0, txt=""):
        """
        Constructor.

        Args:
            at (int, optional): Column position. Defaults to 0.
            txt (str, optional): Name. Defaults to "".
        """

        self.at = at
        self.txt = txt
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, x):
        """
        Updates the count of the things that have been seen so far.

        Args:
            x (str): Thing to check if we've seen so far.
        """

        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        """
        Returns the mode.

        Returns:
            str: Mode.
        """

        return self.mode

    def div(self):
        """
        Returns the entropy.

        Returns:
            float: Entropy.
        """

        def fun(p):
            return p * math.log(p, 2)

        e = 0
        for _, n in self.has.items():
            e = e + fun(n / self.n)

        return -e

    def dist(self, s1, s2):
        """
        Returns the distance between s1 and s2.

        Args:
            s1 (int/float): First symbol to calculate the distance from.
            s2 (int/float): Second symbol to calculate the distance from.

        Returns:
            int: 0 if s1 = s2, 1 otherwise.
        """

        if s1 == "?" and s2 == "?":
            return 1
        elif s1 == s2:
            return 0
        else:
            return 1

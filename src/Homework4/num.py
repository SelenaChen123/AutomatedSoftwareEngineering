import sys


class NUM():
    """
    Summarizes a stream of numbers.
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
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
        self.w = -1 if "-" in txt else 1

    def add(self, n):
        """
        Adds n and updates lo, hi, and other values needed for standard deviation.

        Args:
            n (int): Value to be added.
        """

        if n != "?":
            self.n += 1
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self):
        """
        Returns the mean.

        Returns:
            int: Mean.
        """

        return self.mu

    def div(self):
        """
        Returns the standard deviation using Welford's algorithm.

        Returns:
            float: Standard deviation using Welford's algorithm.
        """

        if (self.m2 < 0 or self.n < 2):
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

    def norm(self, n):
        """
        Normalizes n.

        Args:
            n (int/float): Number to be normalized.

        Returns:
            float: Normalized version of n.
        """

        if n == "?":
            return n
        else:
            return (n - self.lo) / (self.hi - self.lo + 1e-32)

    def dist(self, n1, n2):
        """
        Returns the distance between n1 and n2.

        Args:
            n1 (int/float): First number to calculate the distance from.
            n2 (int/float): Second number to calculate the distance from.

        Returns:
            float: Distance between n1 and n2.
        """

        if n1 == "?" and n2 == "?":
            return 1

        n1 = self.norm(n1)
        n2 = self.norm(n2)

        if n1 == "?":
            if n2 < 0.5:
                n1 = 1
            else:
                n1 = 0
        if n2 == "?":
            if n1 < 0.5:
                n2 = 1
            else:
                n2 = 0

        return abs(n1 - n2)

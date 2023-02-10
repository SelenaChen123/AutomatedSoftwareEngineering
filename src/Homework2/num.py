import sys


class NUM:
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
        self.w = -1 if "-" in self.txt else 1

    def add(self, n):
        """
        Adds n and updates lo, hi, and other values needed for standard deviation.

        Args:
            n (int): Value to be added.
        """

        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self):
        """
        Returns the mean.

        Returns:
            float: Mean.
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

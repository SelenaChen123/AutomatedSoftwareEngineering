import sys


class NUM():
    """
    Summarizes a string of numbers
    """

    def __init__(self, at=0, txt=""):
        """
        Constructor
        """
        self.at = at
        self.txt = txt
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
        self.w = self.txt.find("-")

    def add(self, n):
        """
        Add "n" to the current num, update hi, lo, and other 
            values needed for standard deviation

        Args:
            n (int): value to be added to the num object
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
        Return the mean

        Returns:
            int: mean of the num object
        """
        return self.mu

    def div(self):
        """
        Return standard deviation using Welford's algorithm

        Returns:
            float: returns the standard deviation of the num object
        """
        if (self.m2 < 0 or self.n < 2):
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

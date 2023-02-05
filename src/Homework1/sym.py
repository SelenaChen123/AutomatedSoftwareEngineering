import math


class SYM():
    """
    Summarize a stream of symbols
    """

    def __init__(self):
        """
        Constructor
        """
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, x):
        """
        Update counts of things that have been seen so far

        Args:
            x (str): string that we are seeing if the sym object has seen
        """
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        """
        Return the mode

        Returns:
            int: mean of the sym object
        """
        return self.mode

    def div(self):
        """
        Return the entropy

        Returns:
            float: the entropy of the sym object
        """
        def fun(p):
            return p * math.log(p, 2)

        e = 0
        for _, n in self.has.items():
            e = e + fun(n / self.n)

        return -e

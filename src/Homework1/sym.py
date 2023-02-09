import math


class SYM():
    """
    Summarize a stream of symbols.
    """

    def __init__(self):
        """
        Constructor.
        """

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

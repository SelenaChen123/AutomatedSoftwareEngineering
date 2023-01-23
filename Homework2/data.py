import math
import sys
import random
import re

the = {}
help = """
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2

USAGE:   script.lua  [OPTIONS] [-g ACTION]

OPTIONS:
  -d  --dump    on crash, dump stack = false
  -g  --go      start-up action      = data
  -h  --help    show help            = false
  -s  --seed    random number seed   = 937162211

ACTIONS:
"""


class SYM():
    def __init__(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        def fun(p):
            return p * math.log(p, 2)

        e = 0
        for _, n in self.has.items():
            e = e + fun(n / self.n)

        return -e


class NUM():
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = sys.maxsize
        self.lo = -sys.maxsize

    def add(self, n):
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        if (self.m2 < 0 or self.n < 2):
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5


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


def settings(s):
    t = {}

    for item in re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s):
        k, v = item
        t[k] = coerce(v)

    return t


def cli(options):
    for k, v in options.items():
        v = str(v).lower()

        for n, x in enumerate(sys.argv):
            if x == "-" + k[0] or x == "--" + k:
                if v == "false":
                    v = "true"
                elif v == "true" or n + 1 >= len(sys.argv):
                    v = "false"
                else:
                    v = sys.argv[n + 1]

        options[k] = coerce(v)

    return options


def main(help, funs):
    global the
    saved = {}
    fails = 0

    for k, v in cli(settings(help)).items():
        the[k] = v
        saved[k] = v

    if the["help"]:
        print(help)
    else:
        for what in funs.keys():
            if the["go"] == "all" or what == the["go"]:
                for k, v in saved.items():
                    the[k] = v

                if not funs[what]():
                    fails += 1
                    print("❌ fail:" + what)
                else:
                    print("✅ pass:" + what)


egs = {}


def eg(key, str, fun):
    global help

    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, str)


def eg_the():
    print(str(the))
    return the


def eg_sym():
    sym = SYM()

    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)

    return "a" == sym.mid() and 1.379 == round(sym.div(), 3)


def eg_num():
    num = NUM()

    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)

    return 11 / 7 == num.mid() and 0.787 == round(num.div(), 3)


eg("the", "show settings", eg_the)
eg("sym", "check syms", eg_sym)
eg("num", "check nums", eg_num)

main(help, egs)

from globals import the, help
from sym import SYM
from num import NUM
from data import DATA
from utils import csv


global egs
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


def eg_csv():
    global n
    n = 0

    def function(t):
        global n

        n += len(t)

    csv(the["file"], function)

    return n == 8 * 399


def eg_data():
    data = DATA(the["file"])

    return len(data.rows) == 398 and data.cols.y[1].w == -1 and data.cols.x[1].at == 1 and len(data.cols.x) == 4


def eg_stats():
    data = DATA(the["file"])

    for k, cols in enumerate([data.cols.y, data.cols.x]):
        print(k, "mid", data.stats("mid", cols, 2))
        print("", "div", data.stats("div", cols, 2))

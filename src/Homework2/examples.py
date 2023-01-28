import globals
import sym
import num
import data
import utils


global egs
egs = {}


def eg(key, str, fun):
    egs[key] = fun
    globals.help += "  -g  {}\t{}\n".format(key, str)


def eg_the():
    print(str(globals.the))
    return globals.the


def eg_sym():
    sym1 = sym.SYM()

    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym1.add(x)

    return "a" == sym1.mid() and 1.379 == round(sym1.div(), 3)


def eg_num():
    num1 = num.NUM()

    for x in [1, 1, 1, 1, 2, 2, 3]:
        num1.add(x)

    return 11 / 7 == num1.mid() and 0.787 == round(num1.div(), 3)


def eg_csv():
    global n
    n = 0

    def function(t):
        global n

        n += len(t)

    utils.csv(globals.the["file"], function)

    return n == 8 * 399


def eg_data():
    data1 = data.DATA(globals.the["file"])

    return len(data1.rows) == 398 and data1.cols.y[1].w == -1 and data1.cols.x[1].at == 1 and len(data1.cols.x) == 4


def eg_stats():
    data1 = data.DATA(globals.the["file"])

    for k, cols in enumerate([data1.cols.y, data1.cols.x]):
        print(k, "mid", data1.stats("mid", cols, 2))
        print("", "div", data1.stats("div", cols, 2))

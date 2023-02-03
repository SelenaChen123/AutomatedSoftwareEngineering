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


def eg_data():
    data1 = data.DATA(globals.the["file"])

    return len(data1.rows) == 398 and data1.cols.y[1].w == -1 and data1.cols.x[1].at == 1 and len(data1.cols.x) == 4


def eg_clone():
    data1 = data.DATA(globals.the["file"])
    data2 = data1.clone(data1.rows)

    return len(data1.rows) == len(data2.rows) and data1.cols.y[1].w == data2.cols.y[1].w and data1.cols.x[1].at == data2.cols.x[1].at and len(data1.cols.x) == len(data2.cols.x)


def eg_around():
    data1 = data.DATA(globals.the["file"])
    print(0, 0, str(data1.rows[0].cells))

    for n, t in enumerate(data1.around(data1.rows[0]), 1):
        if n % 50 == 0:
            print(n, round(t["dist"], 2), str(t["row"].cells))


def eg_half():
    data1 = data.DATA(globals.the["file"])
    left, right, A, B, mid, c = data1.half()
    print(len(left), len(right), len(data1.rows))
    print(str(A.cells), c)
    print(str(mid.cells))
    print(str(B.cells))


def eg_cluster():
    data1 = data.DATA(globals.the["file"])
    utils.show(data1.cluster(), "mid", data1.cols.y, 1)


def eg_optimize():
    data1 = data.DATA(globals.the["file"])
    utils.show(data1.sway(), "mid", data1.cols.y, 1)

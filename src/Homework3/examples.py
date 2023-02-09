import globals
import sym
import num
import data
import utils


global egs
egs = {}


def eg(key, str, fun):
    """
    Registers an example.

    Args:
        key (str): Name of the example.
        str (str): Description of the example.
        fun (function): Example function to be registered.
    """

    egs[key] = fun
    globals.help += "  -g  {}\t{}\n".format(key, str)


def eg_the():
    """
    Example determining if the globals load correctly.

    Returns:
        dict: Dictionary containing the global values.
    """

    print(str(globals.the))

    return globals.the


def eg_sym():
    """
    Example testing the symbol type from sym.py.

    Returns:
        bool: True if SYM.mid() = "a" and SYM.div() rounds to 1.379, False otherwise.
    """

    sym1 = sym.SYM()

    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym1.add(x)

    return "a" == sym1.mid() and 1.379 == round(sym1.div(), 3)


def eg_num():
    """
    Example testing the number type from num.py.

    Returns:
        bool: True if NUM.mid() = 11/7 and NUM.div() rounds to 0.787, False otherwise.
    """

    num1 = num.NUM()

    for x in [1, 1, 1, 1, 2, 2, 3]:
        num1.add(x)

    return 11 / 7 == num1.mid() and 0.787 == round(num1.div(), 3)


def eg_data():
    """
    Example testing if DATA is working properly.

    Returns:
        bool: True if DATA has the correct number of rows and certain data points are correct, False otherwise. 
    """

    data1 = data.DATA(globals.the["file"])

    return len(data1.rows) == 398 and data1.cols.y[0].w == -1 and data1.cols.x[1].at == 1 and len(data1.cols.x) == 4


def eg_clone():
    """
    Example testing if DATA is cloned properly.

    Returns:
        bool: True if the cloned DATA has the correct number of rows, certain column weights are correct, certain column locations are correct, and certain column lengths are correct, False otherwise.
    """

    data1 = data.DATA(globals.the["file"])
    data2 = data1.clone(data1.rows)

    return len(data1.rows) == len(data2.rows) and data1.cols.y[1].w == data2.cols.y[1].w and data1.cols.x[1].at == data2.cols.x[1].at and len(data1.cols.x) == len(data2.cols.x)


def eg_around():
    """
    Example testing if sorting nearest neighbors is working properly.
    """

    data1 = data.DATA(globals.the["file"])
    print(0, 0, str(data1.rows[0].cells))

    for n, t in enumerate(data1.around(data1.rows[0]), 1):
        if n % 50 == 0:
            print(n, round(t["dist"], 2), str(t["row"].cells))


def eg_half():
    """
    Example testing if 1-level bi-clustering of DATA is working properly.
    """

    data1 = data.DATA(globals.the["file"])
    left, right, A, B, mid, c = data1.half()
    print(len(left), len(right), len(data1.rows))
    print(str(A.cells), c)
    print(str(mid.cells))
    print(str(B.cells))


def eg_cluster():
    """
    Example testing if N-level bi-clustering of DATA is working properly.
    """

    data1 = data.DATA(globals.the["file"])
    utils.show(data1.cluster(), "mid", data1.cols.y, 1)


def eg_optimize():
    """
    Example testing if semi-supervised optimization of DATA is working properly.
    """

    data1 = data.DATA(globals.the["file"])
    utils.show(data1.sway(), "mid", data1.cols.y, 1)

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


def eg_csv():
    """
    Example testing drawing input from a csv file.

    Returns:
        bool: True if the length of the file is correct, False otherwise.
    """

    global n
    n = 0

    def function(t):
        global n
        n += len(t)

    utils.csv(globals.the["file"], function)

    return n == 8 * 399


def eg_data():
    """
    Example testing if DATA is working properly.

    Returns:
        bool: True if DATA has the correct number of rows and certain data points are correct, False otherwise. 
    """

    data1 = data.DATA(globals.the["file"])
    
    return len(data1.rows) == 398 and data1.cols.y[0].w == -1 and data1.cols.x[1].at == 1 and len(data1.cols.x) == 4


def eg_stats():
    """
    Example testing if DATA.stats() is working properly.
    """

    data1 = data.DATA(globals.the["file"])

    for k, cols in enumerate([data1.cols.y, data1.cols.x]):
        print(k, "mid", data1.stats("mid", cols, 2))
        print("", "div", data1.stats("div", cols, 2))

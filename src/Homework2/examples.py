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
        bool: Boolean determining if the sym1.mid() method returns "a" and if
            sym1.div() method rounds to 1.379.
    """
    sym1 = sym.SYM()

    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym1.add(x)

    return "a" == sym1.mid() and 1.379 == round(sym1.div(), 3)


def eg_num():
    """
    Example testing the number type from num.py.

    Returns:
        bool: Boolean determining if the num1.mid() method returns 11/7 and if
            num1.div() method rounds to 0.787.
    """
    num1 = num.NUM()

    for x in [1, 1, 1, 1, 2, 2, 3]:
        num1.add(x)

    return 11 / 7 == num1.mid() and 0.787 == round(num1.div(), 3)


def eg_csv():
    """
    Example testing the function to draw input from a .csv file

    Returns:
        bool: checks if the length of the output from the csv function is correct 
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
    Example to see if the Data object type is working properly

    Returns:
        bool: checks if the outputted Data object has the correct number of rows and
            if certain data in those rows is accurate 
    """
    data1 = data.DATA(globals.the["file"])

    return len(data1.rows) == 398 and data1.cols.y[1].w == -1 and data1.cols.x[1].at == 1 and len(data1.cols.x) == 4


def eg_stats():
    """
    Example testing the stats function of the data object
    """
    data1 = data.DATA(globals.the["file"])

    for k, cols in enumerate([data1.cols.y, data1.cols.x]):
        print(k, "mid", data1.stats("mid", cols, 2))
        print("", "div", data1.stats("div", cols, 2))

import copy
import globals
import num
import sym
import utils


global egs
egs = {}


def eg(key, str, fun):
    """
    Registers an example.

    Args:
        key (str): Name of the example to be registered.
        str (str): Description of the example to be registered.
        fun (function): Example function to be registered.
    """

    egs[key] = fun
    action = "-g  {}".format(key)
    globals.help += "  {}\t\t{}\n".format(action, str) if len(
        action) < 13 else "  {}\t{}\n".format(action, str)


def eg_the():
    """
    Example testing loading globals.

    Returns:
        dict: Dictionary containing the global values.
    """

    print(str(globals.the))

    return globals.the


def eg_copy():
    """
    Example testing copy().
    """

    t1 = {"a": 1, "b": {"c": 2, "d": [3]}}
    t2 = copy.deepcopy(t1)
    t2["b"]["d"][0] = 10000

    print("b4", t1, "\nafter", t2)


def eg_sym():
    """
    Example testing SYM.

    Returns:
        bool: True if SYM.mid() = "a" and SYM.div() rounds to 1.379, False otherwise.
    """

    sym1 = sym.SYM()

    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym1.add(x)

    return "a" == sym1.mid() and 1.379 == round(sym1.div(), 3)


def eg_num():
    """
    Example testing NUM.

    Returns:
        bool: True if NUM.mid() = 11/7 and NUM.div() rounds to 0.787, False otherwise.
    """

    num1 = num.NUM()

    for x in [1, 1, 1, 1, 2, 2, 3]:
        num1.add(x)

    return 11 / 7 == num1.mid() and 0.787 == round(num1.div(), 3)


def eg_repcols():
    """
    Example testing repCols().
    """

    t = utils.repCols(utils.dofile(globals.the["file"])["cols"])

    for item in t.cols.all:
        print(repr(item))

    for item in t.rows:
        print(repr(item))


def eg_synonyms():
    """
    Example testing DATA.cluster() on repCols().
    """

    utils.show(utils.repCols(utils.dofile(
        globals.the["file"])["cols"]).cluster())


def eg_reprows():
    """
    Example testing repRows().
    """

    t = utils.dofile(globals.the["file"])
    rows = utils.repRows(t, utils.transpose(t["cols"]))

    for item in rows.cols.all:
        print(repr(item))

    for item in rows.rows:
        print(repr(item))


def eg_prototypes():
    """
    Example testing DATA.cluster() on repRows().
    """

    t = utils.dofile(globals.the["file"])
    rows = utils.repRows(t, utils.transpose(t["cols"]))

    utils.show(rows.cluster())


def eg_position():
    """
    Example testing repPlace().
    """

    t = utils.dofile(globals.the["file"])
    rows = utils.repRows(t, utils.transpose(t["cols"]))
    rows.cluster()
    utils.repPlace(rows)


def eg_every():
    """
    Example testing repgrid().
    """

    utils.repgrid(globals.the["file"])

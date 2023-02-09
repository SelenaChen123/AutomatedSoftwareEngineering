import random

import globals
import num
import sym


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
    globals.help += "  -g  {}\t{}\n".format(key, str)


def eg_the():
    """
    Example testing loading globals.

    Returns:
        dict: Dictionary containing the global values.
    """

    print(str(globals.the))

    return globals.the


def eg_rand():
    """
    Example testing the global random seed value.

    Returns:
        bool: True if m1 = m2 and m1 rounds to 0.5, False otherwise.
    """

    num1 = num.NUM()
    num2 = num.NUM()

    random.seed(globals.the["seed"])
    for _ in range(1, 10 ** 3):
        num1.add(random.random())

    random.seed(globals.the["seed"])
    for _ in range(1, 10 ** 3):
        num2.add(random.random())

    m1 = round(num1.mid(), 10)
    m2 = round(num2.mid(), 10)

    return m1 == m2 and .5 == round(m1, 1)


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

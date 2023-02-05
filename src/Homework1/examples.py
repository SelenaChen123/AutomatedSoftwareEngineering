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
        key (str): Name of the example.
        str (str): Description of the example.
        fun (function): Example function to be registered.
    """
    egs[key] = fun
    globals.help += "  -g  {}\t{}\n".format(key, str)


def eg_the():
    """
    Example determining if the globals panel 
        Loads correctly

    Returns:
        dict: Dictionary containing the globals values
    """
    print(str(globals.the))
    return globals.the


def eg_rand():
    """
    Example testing the random seed value from globals

    Returns:
        bool: boolean determining if m1 is equal to m2 and if m1 rounds to 0.5
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
    Example testing the symbol type from sym.py

    Returns:
        bool: boolean determining if the sym1.mid() method returns "a" and if
            sym1.div() method rounds to 1.379
    """
    sym1 = sym.SYM()

    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym1.add(x)

    return "a" == sym1.mid() and 1.379 == round(sym1.div(), 3)


def eg_num():
    """
    Example testing the number type from num.py

    Returns:
        bool: boolean determining if the num1.mid() method returns 11/7 and if
            num1.div() method rounds to 0.787
    """
    num1 = num.NUM()

    for x in [1, 1, 1, 1, 2, 2, 3]:
        num1.add(x)

    return 11 / 7 == num1.mid() and 0.787 == round(num1.div(), 3)

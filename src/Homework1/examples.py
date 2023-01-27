import random

from globals import the, help
from num import NUM
from sym import SYM


global egs
egs = {}


def eg(key, str, fun):
    global help

    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, str)


def eg_the():
    print(str(the))
    return the


def eg_rand():
    num1 = NUM()
    num2 = NUM()

    random.seed(the["seed"])
    for _ in range(1, 10 ** 3):
        num1.add(random.random())

    random.seed(the["seed"])
    for _ in range(1, 10 ** 3):
        num2.add(random.random())

    m1 = round(num1.mid(), 10)
    m2 = round(num2.mid(), 10)

    return m1 == m2 and .5 == round(m1, 1)


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

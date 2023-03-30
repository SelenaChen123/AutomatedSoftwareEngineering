import random

import creation
import query
import stats
import utils

global egs
egs = {}


def eg(key, fun):
    """
    Registers an example.

    Args:
        key (str): Name of the example to be registered.
        fun (function): Example function to be registered.
    """

    egs[key] = fun


def eg_ok(n=1):
    """
    Sets the random seed.

    Args:
        n (int, optional): Random seed. Defaults to 1.
    """

    random.seed(n)


def eg_sample():
    """
    Example testing samples().
    """

    for _ in range(10):
        print("\t", "".join(utils.samples(["a", "b", "c", "d", "e"])))


def eg_num():
    """
    Example testing NUM().
    """

    n = creation.NUM([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print("", n["n"], n["mu"], n["sd"], sep="\t")


def eg_gauss():
    """
    Example testing gaussian().
    """

    t = []

    for _ in range(10 ** 4):
        t.append(utils.gaussian(10, 2))

    n = creation.NUM(t)

    print("", n["n"], n["mu"], n["sd"], sep="\t")


def eg_bootmu():
    """
    Example testing cliffsDelta() and bootstrap().
    """

    a = []
    b = []

    for _ in range(100):
        a.append(utils.gaussian(10, 1))

    print("", "mu", "sd", "cliffs", "boot", "both", sep="\t")
    print("", "--", "--", "------", "----", "----", sep="\t")

    for mu in range(100, 111):
        b = []

        for _ in range(100):
            b.append(utils.gaussian(mu / 10, 1))

        cl = utils.cliffsDelta(a, b)
        bs = stats.bootstrap(a, b)

        print("", mu / 10, 1, cl, bs, cl and bs, sep="\t")


def eg_basic():
    """
    Example testing bootstrap() with hardcoded values.
    """

    print("", "True", stats.bootstrap([8, 7, 6, 2, 5, 8, 7, 3], [
          8, 7, 6, 2, 5, 8, 7, 3]), utils.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]), sep="\t")
    print("", "False", stats.bootstrap([8, 7, 6, 2, 5, 8, 7, 3], [
          9, 9, 7, 8, 10, 9, 6]), utils.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]), sep="\t")
    print("", "False", stats.bootstrap([0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6], [0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9]), utils.cliffsDelta(
        [0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6], [0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9]), sep="\t")


def eg_pre():
    """
    Example testing bootstrap() with Gaussian values.
    """

    print("\teg3")

    d = 1

    for _ in range(10):
        t1 = []
        t2 = []

        for _ in range(32):
            t1.append(utils.gaussian(10, 1))
            t2.append(utils.gaussian(d * 10, 1))

        print("", "", d, d < 1.1, stats.bootstrap(
            t1, t2), stats.bootstrap(t1, t1), sep="\t")

        d = round(d + .05, 2)


def eg_five():
    """
    Example testing scottKnot() with different central tendencies.
    """

    for rx in (stats.tiles(stats.scottKnot([creation.RX([0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6], "rx1"), creation.RX([0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9], "rx2"), creation.RX([0.15, 0.25, 0.4, 0.35, 0.15, 0.25, 0.4, 0.35], "rx3"), creation.RX([0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9], "rx4"), creation.RX([0.1, 0.2, 0.3, 0.4, 0.1, 0.2, 0.3, 0.4], "rx5")]))):
        print("", rx["name"], rx["rank"], rx["show"], sep="\t")


def eg_six():
    """
    Example testing scottKnot() with the same central tendencies.
    """

    for rx in (stats.tiles(stats.scottKnot([creation.RX([101, 100, 99, 101, 99.5, 101, 100, 99, 101, 99.5], "rx1"), creation.RX([101, 100, 99, 101, 100, 101, 100, 99, 101, 100], "rx2"), creation.RX([101, 100, 99.5, 101, 99, 101, 100, 99.5, 101, 99], "rx3"), creation.RX([101, 100, 99, 101, 100, 101, 100, 99, 101, 100], "rx4")]))):
        print("", rx["name"], rx["rank"], rx["show"], sep="\t")


def eg_tiles():
    """
    Example testing scottKnot().
    """

    rxs = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []

    for _ in range(1000):
        a.append(utils.gaussian(10, 1))

    for _ in range(1000):
        b.append(utils.gaussian(10.1, 1))

    for _ in range(1000):
        c.append(utils.gaussian(20, 1))

    for _ in range(1000):
        d.append(utils.gaussian(30, 1))

    for _ in range(1000):
        e.append(utils.gaussian(30.1, 1))

    for _ in range(1000):
        f.append(utils.gaussian(10, 1))

    for _ in range(1000):
        g.append(utils.gaussian(10, 1))

    for _ in range(1000):
        h.append(utils.gaussian(40, 1))

    for _ in range(1000):
        i.append(utils.gaussian(40, 3))

    for _ in range(1000):
        j.append(utils.gaussian(10, 1))

    for k, v in enumerate([a, b, c, d, e, f, g, h, i, j]):
        rxs.append(creation.RX(v, "rx{}".format(k + 1)))

    rxs = sorted(rxs, key=lambda x: query.mid(x))

    for rx in stats.tiles(rxs):
        print("", rx["name"], rx["show"], sep="\t")


def eg_sk():
    """
    Example testing scottKnot() ranks.
    """

    rxs = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []

    for _ in range(1000):
        a.append(utils.gaussian(10, 1))

    for _ in range(1000):
        b.append(utils.gaussian(10.1, 1))

    for _ in range(1000):
        c.append(utils.gaussian(20, 1))

    for _ in range(1000):
        d.append(utils.gaussian(30, 1))

    for _ in range(1000):
        e.append(utils.gaussian(30.1, 1))

    for _ in range(1000):
        f.append(utils.gaussian(10, 1))

    for _ in range(1000):
        g.append(utils.gaussian(10, 1))

    for _ in range(1000):
        h.append(utils.gaussian(40, 1))

    for _ in range(1000):
        i.append(utils.gaussian(40, 3))

    for _ in range(1000):
        j.append(utils.gaussian(10, 1))

    for k, v in enumerate([a, b, c, d, e, f, g, h, i, j]):
        rxs.append(creation.RX(v, "rx{}".format(k)))

    for rx in stats.tiles(stats.scottKnot(rxs)):
        print("", rx["rank"], rx["name"], rx["show"], sep="\t")

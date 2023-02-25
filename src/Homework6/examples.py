import clustering
import creation
import discretization
import globals
import optimization
import query
import update
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
    globals.help += "  {}\t{}\n".format(action, str)


def eg_Is():
    """
    Example testing loading globals.

    Returns:
        dict: Dictionary containing the global values.
    """

    print(str(globals.the))

    return globals.the


def eg_rand():
    """
    Example testing rand().
    """

    globals.seed = 1
    t = []

    for _ in range(1000):
        t.append(utils.rint(100))

    globals.seed = 1
    u = []

    for _ in range(1000):
        u.append(utils.rint(100))

    for k, v in enumerate(t):
        assert v == u[k]


def eg_some():
    """
    Example testing some().
    """

    globals.the["Max"] = 32
    num1 = creation.NUM()

    for i in range(10000):
        update.add(num1, i + 1)

    print(query.has(num1))


def eg_nums():
    """
    Example testing NUM().

    Returns:
        bool: True if mid(num1) rounds to .5 and mid(num1) > mid(num2), False otherwise.
    """

    num1 = creation.NUM()
    num2 = creation.NUM()

    for _ in range(10000):
        update.add(num1, utils.rand())

    for _ in range(10000):
        update.add(num2, utils.rand() ** 2)

    print(1, round(query.mid(num1), 2), round(query.div(num1), 2))
    print(2, round(query.mid(num2), 2), round(query.div(num2), 2))

    return .5 == round(query.mid(num1), 2) and query.mid(num1) > query.mid(num2)


def eg_syms():
    """
    Example testing SYM().

    Returns:
        bool: True if div(sym) rounds to 1.38, False otherwise.
    """

    sym = update.adds(creation.SYM(), ["a", "a", "a", "a", "b", "b", "c"])

    print(query.mid(sym), round(query.div(sym), 2))

    return 1.38 == round(query.div(sym), 2)


def eg_csv():
    """
    Example testing csv().

    Returns:
        bool: True if the length of the file is correct, False otherwise.
    """

    global n
    n = 0

    def f(t):
        global n
        n += len(t)

    utils.csv(globals.the["file"], f)

    return 3192 == n


def eg_data():
    """
    Example testing read().
    """

    data = creation.read(globals.the["file"])
    col = data["cols"]["x"][0]

    print(col["lo"], col["hi"], query.mid(col), query.div(col))
    print(query.stats(data))


def eg_clone():
    """
    Example testing clone().
    """

    data1 = creation.read(globals.the["file"])
    data2 = creation.clone(data1, data1["rows"])

    print(query.stats(data1))
    print(query.stats(data2))


def eg_cliffs():
    """
    Example testing cliffsDelta().
    """

    assert not utils.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [
                                 8, 7, 6, 2, 5, 8, 7, 3]), "1"

    assert utils.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [
                             9, 9, 7, 8, 10, 9, 6]), "2"

    t1 = []
    t2 = []

    for _ in range(1000):
        t1.append(utils.rand())

    for _ in range(1000):
        t2.append(utils.rand() ** .5)

    assert not utils.cliffsDelta(t1, t1), "3"
    assert utils.cliffsDelta(t1, t2), "4"

    diff = False
    j = 1

    while not diff:
        t3 = list(map(lambda x: x * j, t1))
        diff = utils.cliffsDelta(t1, t3)

        print(">", round(j, 2), diff)

        j *= 1.025


def eg_dist():
    """
    Example testing dist().
    """

    data = creation.read(globals.the["file"])
    num = creation.NUM()

    for row in data["rows"]:
        update.add(num, query.dist(data, row, data["rows"][0]))

    print({"lo": num["lo"], "hi": num["hi"], "mid": round(
        query.mid(num), 2), "div": round(query.div(num), 2)})


def eg_half():
    """
    Example testing half().
    """

    data = creation.read(globals.the["file"])
    left, right, _, _, _ = clustering.half(data)

    print(len(left), len(right))

    l = creation.clone(data, left)
    r = creation.clone(data, right)

    print("l", query.stats(l))
    print("r", query.stats(r))


def eg_tree():
    """
    Example testing tree().
    """

    clustering.showTree(clustering.tree(creation.read(globals.the["file"])))


def eg_sway():
    """
    Example testing sway().
    """

    data = creation.read(globals.the["file"])
    best, rest = optimization.sway(data)

    print("\nall ", query.stats(data))
    print("    ", query.stats(data, query.div))
    print("\nbest", query.stats(best))
    print("    ", query.stats(best, query.div))
    print("\nrest", query.stats(rest))
    print("    ", query.stats(rest, query.div))
    print("\nall != best?", utils.diffs(best["cols"]["y"], data["cols"]["y"]))
    print("best != rest?", utils.diffs(best["cols"]["y"], rest["cols"]["y"]))


def eg_bins():
    """
    Example testing bins().
    """

    b4 = ""
    data = creation.read(globals.the["file"])
    best, rest = optimization.sway(data)

    print("all", "", "", "", {"best": len(
        best["rows"]), "rest": len(rest["rows"])})

    for t in discretization.bins(data["cols"]["x"], {"best": best["rows"], "rest": rest["rows"]}):
        for Range in t:
            if Range["txt"] != b4:
                print()

            b4 = Range["txt"]

            print(Range["txt"], Range["lo"], Range["hi"], round(query.value(
                Range["y"]["has"], len(best["rows"]), len(rest["rows"]), "best"), 2), Range["y"]["has"])


def eg_xpln():
    return "NOT YET IMPLEMENTED"

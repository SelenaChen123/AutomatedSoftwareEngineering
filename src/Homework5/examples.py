import clustering
import creation
import discretization
import globals
import optimization
import update
import utils
import query

global egs
egs = {}


def eg(key, str, fun):
    egs[key] = fun
    action = "-g  {}".format(key)
    globals.help += "  {}\t{}\n".format(action, str)


def eg_the():
    print(str(globals.the))

    return globals.the


def eg_rand():
    utils.seed = 1
    t = []

    for _ in range(1000):
        t.append(utils.rint(100))

    utils.seed = 1
    u = []

    for _ in range(1000):
        u.append(utils.rint(100))

    for k, v in enumerate(t):
        assert v == u[k]


def eg_some():
    globals.the["Max"] = 32
    num1 = creation.NUM()

    for i in range(10000):
        update.add(num1, i)

    print(query.has(num1))


def eg_nums():
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
    sym = update.adds(creation.SYM(), ["a", "a", "a", "a", "b", "b", "c"])

    print(query.mid(sym), round(query.div(sym), 2))

    return 1.38 == round(query.div(sym), 2)


def eg_csv():
    n = 0

    def f(t):
        n += len(t)

    utils.csv(globals.the["file"], f)

    return 3192 == n


def eg_data():
    data = creation.read(globals.the["file"])
    col = data.cols.x[1]

    print(col.lo, col.hi, query.mid(col), query.div(col))
    print(query.stats(data))


def eg_clone():
    data1 = creation.read(globals.the["file"])
    data2 = creation.clone(data1, data1.rows)

    print(query.stats(data1))
    print(query.stats(data2))


def eg_cliffs():
    assert (False == utils.cliffsDelta(
        [8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]), "1")

    assert (True == utils.cliffsDelta(
        [8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]), "2")

    t1 = []
    t2 = []

    for _ in range(1000):
        t1.append(utils.rand())

    for _ in range(1000):
        t2.append(utils.rand() ** .5)

    assert (False == utils.cliffsDelta(t1, t1), "3")
    assert (True == utils.cliffsDelta(t1, t2), "4")

    diff = False
    j = 1

    while not diff:
        t3 = list(map(lambda x: x * j, t1))
        diff = utils.cliffsDelta(t1, t3)

        print(">", round(j, 2), diff)

        j *= 1.025


def eg_dist():
    data = creation.read(globals.the["file"])
    num = creation.NUM()

    for row in data.rows.values():
        update.add(num, query.dist(data, row, data.rows[1]))

    print({"lo": num.lo, "hi": num.hi, "mid": round(
        query.mid(num), 2), "div": round(query.div(num), 2)})


def eg_half():
    data = creation.read(globals.the["file"])
    left, right, _, _, _ = clustering.half(data)

    print(len(left), len(right))

    l = creation.clone(data, left)
    r = creation.clone(data, right)

    print("l", query.stats(l))
    print("r", query.stats(r))


def eg_tree():
    clustering.showTree(clustering.tree(creation.read(globals.the["file"])))


def eg_sway():
    data = creation.read(globals.the["file"])
    best, rest = optimization.sway(data)

    print("\nall ", query.stats(data))
    print("    ", query.stats(data, query.div))
    print("\nbest", query.stats(best))
    print("    ", query.stats(best, query.div))
    print("\nrest", query.stats(rest))
    print("    ", query.stats(rest, query.div))
    print("\nall != best?", utils.diffs(best.cols.y, data.cols.y))
    print("best != rest?", utils.diffs(best.cols.y, rest.cols.y))


def eg_bins(data, best, rest):
    data = creation.read(globals.the["file"])
    best, rest = optimization.sway(data)

    print("all", "", "", "", {"best": len(
        best["rows"]), "rest": len(rest["rows"])})

    for t in [discretization.bins(data.cols.x, {"best": best["rows"], "rest": rest["rows"]})]:
        for Range in t:
            print(Range["txt"], Range["lo"], Range["hi"], round(query.value(
                Range["y"]["has"], len(best["rows"]), len(rest["rows"]), "best"), Range["y"]["has"]))

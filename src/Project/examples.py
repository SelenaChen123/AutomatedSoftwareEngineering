import random

import clustering
import creation
import discretization
import globals
import optimization
import query
import sets
import update
import utils
import stats

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

    print(str(globals.Is))

    return globals.Is


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

    globals.Is["Max"] = 32
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

    utils.csv(globals.Is["file"], f)

    return 3192 == n if "auto93.csv" in globals.Is["file"][globals.Is["file"].rfind("/")] else True


def eg_data():
    """
    Example testing DATA().
    """

    data = creation.DATA(globals.Is["file"])
    col = data["cols"]["x"][0]

    # print(col["lo"], col["hi"], query.mid(col), query.div(col))
    print(query.mid(col), query.div(col))
    print(query.stats(data))


def eg_clone():
    """
    Example testing replicating DATA().
    """

    data1 = creation.DATA(globals.Is["file"])
    data2 = creation.DATA(data1, data1["rows"])

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

    data = creation.DATA(globals.Is["file"])
    num = creation.NUM()

    for row in data["rows"]:
        update.add(num, query.dist(data, row, data["rows"][0]))

    print({"lo": num["lo"], "hi": num["hi"], "mid": round(
        query.mid(num), 2), "div": round(query.div(num), 2)})


def eg_half():
    """
    Example testing half().
    """

    data = creation.DATA(globals.Is["file"])
    left, right, _, _, _, _ = clustering.half(data)

    print(len(left), len(right))

    l = creation.DATA(data, left)
    r = creation.DATA(data, right)

    print("l", query.stats(l))
    print("r", query.stats(r))


def eg_tree():
    """
    Example testing tree().
    """

    clustering.showTree(clustering.tree(creation.DATA(globals.Is["file"])))


def eg_sway():
    """
    Example testing sway().
    """

    data = creation.DATA(globals.Is["file"])
    best, rest, _ = optimization.sway(data)

    print("\nall ", query.stats(data))
    print("    ", query.stats(data, query.div))
    print("\nbest", query.stats(best))
    print("    ", query.stats(best, query.div))
    print("\nrest", query.stats(rest))
    print("    ", query.stats(rest, query.div))
    print(best["cols"]["y"])
    print("\nall != best?", utils.diffs(best["cols"]["y"], data["cols"]["y"]))
    print("best != rest?", utils.diffs(best["cols"]["y"], rest["cols"]["y"]))


def eg_bins():
    """
    Example testing bins().
    """

    b4 = ""
    data = creation.DATA(globals.Is["file"])
    best, rest, _ = optimization.sway(data)

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
    """
    Example testing xpln().
    """

    data = creation.DATA(globals.Is["file"])
    rule = None

    while (rule == None):
        best, rest, evals = optimization.sway(data)
        rule, _ = sets.xpln(data, best, rest)

    print("\n-----------\nexplain=", sets.showRule(rule))

    data1 = creation.DATA(data, sets.selects(rule, data["rows"]))

    print("all               ", query.stats(
        data), query.stats(data, query.div))
    print("sway with {} evals".format(evals),
          query.stats(best), query.stats(best, query.div))
    print("xpln on   {} evals".format(evals), query.stats(
        data1), query.stats(data1, query.div))

    top, _ = query.betters(data, len(best["rows"]))
    top = creation.DATA(data, top)

    print("sort with {} evals".format(len(data["rows"])), query.stats(
        top), query.stats(top, query.div))


def eg_sample():
    """
    Example testing samples().
    """

    for _ in range(10):
        print("\t", "".join(utils.samples(["a", "b", "c", "d", "e"])))


def eg_gauss():
    """
    Example testing gaussian().
    """

    t = []

    for _ in range(10 ** 4):
        t.append(utils.gaussian(10, 2))

    n = creation.NUM(t=t)

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

        print(mu, mu / 10, 1, cl, bs, cl and bs, sep="\t")


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

    rxs = sorted(rxs, key=lambda x: query.mid1(x))

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


def eg_report():
    data = creation.DATA(globals.Is["file"])
    results = {"all": {"data": None, "sums": [], "to": [{"k": "all", "results": []}, {"k": "sway1", "results": []}, {"k": "sway2", "results": []}]}, "sway1": {"data": None, "sums": [], "to": [{"k": "sway2", "results": []}, {"k": "xpln1", "results": []}, {
        "k": "top", "results": []}]}, "xpln1": {"data": None, "sums": [], "to": []}, "sway2": {"data": None, "sums": [], "to": [{"k": "xpln2", "results": []}]}, "xpln2": {"data": None, "sums": [], "to": []}, "top": {"data": None, "sums": [], "to": []}}
    rule1 = None
    iterations = 1

    for i in range(iterations):
        globals.seed = random.randint(0, 1000)

        while (rule1 == None):
            best1, rest1, _ = optimization.sway(data)
            rule1, _ = sets.xpln(data, best1, rest1, False)

        data1 = creation.DATA(data, sets.selects(rule1, data["rows"]))
        top, _ = query.betters(data, len(best1["rows"]))
        top = creation.DATA(data, top)

        rule2 = None

        while (rule2 == None):
            best2, rest2, _ = optimization.sway2(data)
            rule2, _ = sets.xpln(data, best2, rest2, False)

        data2 = creation.DATA(data, sets.selects(rule2, data["rows"]))

        results["all"]["data"] = data
        results["sway1"]["data"] = best1
        results["xpln1"]["data"] = data1
        results["sway2"]["data"] = best2
        results["xpln2"]["data"] = data2
        results["top"]["data"] = top

        for k in results:
            stat = query.stats(results[k]["data"])
            del stat["N"]

            if i == 0:
                results[k]["sums"] = stat.values()
            else:
                results[k]["sums"] = [old + new for old,
                                      new in zip(results[k]["sums"], stat.values())]

    print("", end="")

    for y in sorted([data["cols"]["y"][i]["txt"] for i in range(len(data["cols"]["y"]))]):
        print(y, end=" ")

    for k in results:
        print("\n{} ".format(k) if k !=
              "all" and k != "top" else "\n{} ".format(k), end="")

        for value in results[k]["sums"]:
            print(round(value / iterations, 2), end=" ")

    print("\n\n", end="")

    for y in sorted([data["cols"]["y"][i]["txt"] for i in range(len(data["cols"]["y"]))]):
        print(y, end=" ")

    for k in results:
        for to in range(len(results[k]["to"])):
            result = []

            for i in range(len(data["cols"]["y"])):
                y0 = results[k]["data"]["cols"]["y"][i]["has"]
                z0 = results[results[k]["to"][to]
                             ["k"]]["data"]["cols"]["y"][i]["has"]

                result.append("=" if not (stats.bootstrap(y0, z0)
                                          and utils.cliffsDelta(y0, z0)) else "≠")

            results[k]["to"][to]["results"] = result

            if results[k]["to"][to]["k"] != "top":
                print("\n{} {} ".format(k, results[k]["to"][to]["k"]), end="")

                for result in results[k]["to"][to]["results"]:
                    print(result, end=" ")

    print("\nsway1 top ", end="")

    for result in results["sway1"]["to"][2]["results"]:
        print(result, end=" ")

    print()


def eg_read():
    names = ["all", "sway1", "xpln1", "sway2", "xpln2", "top"]
    num_iterations = 20
    num_ys = 4
    results = []
    report = []

    for iteration_num in range(num_iterations):
        with open("../../etc/out/project1.{}.out".format(iteration_num + 1), encoding="UTF-8") as f:
            lines = f.readlines()
            summary = []

            for line in lines:
                tokens = line.split()

                if len(tokens) > 0 and tokens[0] in names:
                    info = []

                    for token in tokens[1 if "." in tokens[len(tokens) - 1] else 2:]:
                        info.append(token)

                    summary.append(info)

            results.extend(summary)

    for i, line in enumerate(results):
        break
        # if "." in line[0]:
            # print(i, line)
        # else:
        #     print("--------", end=" ")

    report = [[0 for _ in range(num_ys)], [0 for _ in range(num_ys)], [0 for _ in range(num_ys)], [0 for _ in range(num_ys)], [0 for _ in range(num_ys)], [0 for _ in range(num_ys)], ["" for _ in range(
        num_ys)], ["" for _ in range(num_ys)], ["" for _ in range(num_ys)], ["" for _ in range(num_ys)], ["" for _ in range(num_ys)], ["" for _ in range(num_ys)], ["" for _ in range(num_ys)]]

    print(results[0 + 1])
    report[0] = [
        round(sum([float(results[i * 13][0])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[i * 13][1])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[i * 13][2])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[i * 13][3])
                   for i in range(num_iterations - 1)]) / num_iterations, 2)
    ]

    print(report[0])

    report[1] = [
        round(sum([float(results[(i * 13) + 1][0])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 1][1])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 1][2])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 1][3])
                   for i in range(num_iterations - 1)]) / num_iterations, 2)
    ]

    report[2] = [
        round(sum([float(results[(i * 13) + 2][0])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 2][1])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 2][2])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 2][3])
                   for i in range(num_iterations - 1)]) / num_iterations, 2)
    ]

    print(results[39])

    report[3] = [
        round(sum([float(results[(i * 13) + 3][0])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 3][1])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 3][2])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 3][3])
                   for i in range(num_iterations - 1)]) / num_iterations, 2)
    ]

    report[4] = [
        round(sum([float(results[(i * 13) + 4][0])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 4][1])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 4][2])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 4][3])
                   for i in range(num_iterations - 1)]) / num_iterations, 2)
    ]

    report[5] = [
        round(sum([float(results[(i * 13) + 5][0])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 5][1])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 5][2])
                   for i in range(num_iterations - 1)]) / num_iterations, 2),
        round(sum([float(results[(i * 13) + 5][3])
                   for i in range(num_iterations - 1)]) / num_iterations, 2)
    ]

    for line in report:
        print(line)

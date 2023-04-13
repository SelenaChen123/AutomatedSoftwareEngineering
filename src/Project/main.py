import math
import re
import sys

import examples
import globals
import utils


def settings(s):
    """
    Parses the global help string to extract a dictionary of options.

    Args:
        s (str): String containing the global options to be parsed.

    Returns:
        dict: Dictionary containing the global options.
    """

    t = {}

    for item in re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s):
        k, v = item
        t[k] = utils.coerce(v)

    return t


def cli(options):
    """
    Updates t with the global options from the command line.

    Args:
        options (dict): Dictionary containing the global options.

    Returns:
        dict: Modified dictionary containing the global options from the command line.
    """

    for k, v in options.items():
        v = str(v).lower()

        for n, x in enumerate(sys.argv):
            if x == "-" + k[0] or x == "--" + k:
                if v == "false":
                    v = "true"
                elif v == "true" or n + 1 >= len(sys.argv):
                    v = "false"
                else:
                    v = sys.argv[n + 1]

        options[k] = utils.coerce(v)

    return options


def main(help, funs):
    """
    Fills in the global dictionary, updates them from the command line, runs the examples, prints the number of tests that failed, and resets the random number seed and settings.

    Args:
        help (str): String containing the default global options.
        funs (dict): Contains the list of examples to be run as tests.
    """

    y = 0
    n = 0
    saved = {}

    for k, v in cli(settings(help)).items():
        globals.Is[k] = v
        saved[k] = v

    if globals.Is["help"]:
        print(help)
    else:
        for pair in funs.keys():
            if globals.Is["go"] == "all" or pair == globals.Is["go"]:
                for k, v in saved.items():
                    globals.Is[k] = v

                globals.seed = globals.Is["seed"]

                if funs[pair]() == False:
                    n += 1
                    print("❌ FAIL " + pair)
                else:
                    y += 1
                    print("✅ PASS " + pair)

    if y + n > 0:
        print("\n🔆 {}\n".format({"pass": y, "fail": n,
              "success": 100 * y / math.floor(y + n)}))

    return n


if __name__ == "__main__":
    """
    Starting point of the program. Generates examples and calls the main function.
    """

    examples.eg("Is", "show options", examples.eg_Is)
    examples.eg("rand", "demo random number generation", examples.eg_rand)
    examples.eg("some", "demo of reservoir sampling", examples.eg_some)
    examples.eg("nums", "demo of NUM", examples.eg_nums)
    examples.eg("syms", "demo SYMS", examples.eg_syms)
    examples.eg("csv", "reading csv files", examples.eg_csv)
    examples.eg("data", "showing data sets", examples.eg_data)
    examples.eg("clone", "replicate structure of a DATA", examples.eg_clone)
    examples.eg("cliffs", "stats tests", examples.eg_cliffs)
    examples.eg("dist", "distance test", examples.eg_dist)
    examples.eg("half", "divide data in half", examples.eg_half)
    examples.eg("tree", "make and show tree of clusters", examples.eg_tree)
    examples.eg("sway", "optimizing", examples.eg_sway)
    examples.eg("bins", "find deltas between best and rest", examples.eg_bins)
    examples.eg("xpln", "explore explanation sets", examples.eg_xpln)

    main(globals.help, examples.egs)

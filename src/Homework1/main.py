import sys
import re

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

    saved = {}
    fails = 0

    for k, v in cli(settings(help)).items():
        globals.the[k] = v
        saved[k] = v

    if globals.the["help"]:
        print(help)
    else:
        for what in funs:
            if globals.the["go"] == "all" or what == globals.the["go"]:
                for k, v in saved.items():
                    globals.the[k] = v

                if not funs[what]():
                    fails += 1
                    print("❌ fail: " + what)
                else:
                    print("✅ pass: " + what)


if __name__ == '__main__':
    """
    Starting point of the program. Generates examples and calls the main function.
    """

    examples.eg("the", "show settings", examples.eg_the)
    examples.eg("rand", "generate, reset, regenerate same", examples.eg_rand)
    examples.eg("sym", "check syms", examples.eg_sym)
    examples.eg("num", "check nums", examples.eg_num)

    main(globals.help, examples.egs)

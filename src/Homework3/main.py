import sys
import re

import globals
import utils
import examples


def settings(s):
    t = {}

    for item in re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s):
        k, v = item
        t[k] = utils.coerce(v)

    return t


def cli(options):
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
    saved = {}
    fails = 0

    for k, v in cli(settings(help)).items():
        globals.the[k] = v
        saved[k] = v

    if globals.the["help"]:
        print(help)
    else:
        for what in funs.keys():
            if globals.the["go"] == "all" or what == globals.the["go"]:
                for k, v in saved.items():
                    globals.the[k] = v

                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:" + what)
                else:
                    print("✅ pass:" + what)


if __name__ == '__main__':
    examples.eg("the", "show settings", examples.eg_the)
    examples.eg("sym", "check syms", examples.eg_sym)
    examples.eg("num", "check nums", examples.eg_num)
    examples.eg("data", "read DATA csv", examples.eg_data)
    examples.eg("clone", "duplicate structure", examples.eg_clone)
    examples.eg("around", "sorting nearest neighbors", examples.eg_around)
    examples.eg("half", "1-level bi-clustering", examples.eg_half)
    examples.eg("cluster", "N-level bi-clustering", examples.eg_cluster)
    examples.eg("optimize", "semi-supervised optimization", examples.eg_optimize)

    main(globals.help, examples.egs)

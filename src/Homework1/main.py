import sys
import re

from globals import the, help
from utils import coerce
from examples import egs, eg, eg_the, eg_rand, eg_sym, eg_num


def settings(s):
    t = {}

    for item in re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s):
        k, v = item
        t[k] = coerce(v)

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

        options[k] = coerce(v)

    return options


def main(help, funs):
    saved = {}
    fails = 0

    for k, v in cli(settings(help)).items():
        the[k] = v
        saved[k] = v

    if the["help"]:
        print(help)
    else:
        for what in funs.keys():
            if the["go"] == "all" or what == the["go"]:
                for k, v in saved.items():
                    the[k] = v

                if not funs[what]():
                    fails += 1
                    print("❌ fail:" + what)
                else:
                    print("✅ pass:" + what)


if __name__ == '__main__':
    eg("the", "show settings", eg_the)
    eg("rand", "generate, reset, regenerate same", eg_rand)
    eg("sym", "check syms", eg_sym)
    eg("num", "check nums", eg_num)

    main(help, egs)

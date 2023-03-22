import examples


def main(funs):
    """
    Runs the examples.

    Args:
        funs (dict): Contains the list of examples to be run as tests.
    """

    for k, fun in funs.items():
        funs["ok"]()

        print("\n" + k)

        fun()


if __name__ == "__main__":
    """
    Starting point of the program. Generates examples and calls the main function.
    """

    examples.eg("ok", examples.eg_ok)
    examples.eg("num", examples.eg_num)
    examples.eg("gauss", examples.eg_gauss)
    examples.eg("bootmu", examples.eg_bootmu)
    examples.eg("basic", examples.eg_basic)
    examples.eg("pre", examples.eg_pre)
    examples.eg("five", examples.eg_five)
    examples.eg("six", examples.eg_six)
    examples.eg("tiles", examples.eg_tiles)
    examples.eg("sk", examples.eg_sk)

    main(examples.egs)
